#!/usr/bin/env python3
"""
SRL Muse EEG Connection & Live Stream
======================================
Connects to Muse 2 via BrainFlow, streams live EEG data,
computes alpha/theta power in real time, and saves session data.

Usage:
  python3 tools/muse-connect.py              # Connect + 60s recording
  python3 tools/muse-connect.py --duration 120  # 2-minute recording
  python3 tools/muse-connect.py --live         # Live stream to terminal
  python3 tools/muse-connect.py --plot         # Plot after recording

Muse 2 Channels:
  TP9  (left ear)   = channel 1
  AF7  (left forehead) = channel 2
  AF8  (right forehead) = channel 3
  TP10 (right ear)  = channel 4

BrainFlow Board: MUSE_2_BLED_BOARD (22) — uses native macOS Bluetooth
"""

import argparse
import time
import sys
import os
import json
from datetime import datetime

import numpy as np
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds, LogLevels
from brainflow.data_filter import DataFilter, FilterTypes, WindowOperations


# ─── Channel map ───
CHANNEL_NAMES = {1: "TP9 (L ear)", 2: "AF7 (L forehead)", 3: "AF8 (R forehead)", 4: "TP10 (R ear)"}
BOARD_ID = BoardIds.MUSE_2_BLED_BOARD  # Change to MUSE_S_BLED_BOARD for Muse S


def compute_band_powers(data, sampling_rate, channel):
    """Compute delta, theta, alpha, beta, gamma power for a single channel."""
    # Apply bandpass filter 1-50 Hz
    filtered = data[channel].copy()
    DataFilter.perform_bandpass(filtered, sampling_rate, 25.0, 24.0, 4, FilterTypes.BUTTERWORTH, 0)

    # Use PSD via Welch's method
    nfft = DataFilter.get_nearest_power_of_two(sampling_rate)
    psd = DataFilter.get_psd_welch(data[channel], nfft, nfft // 2, sampling_rate, WindowOperations.HAMMING)

    # Band power extraction
    delta = DataFilter.get_band_power(psd, 1.0, 4.0)
    theta = DataFilter.get_band_power(psd, 4.0, 8.0)
    alpha = DataFilter.get_band_power(psd, 8.0, 13.0)
    beta = DataFilter.get_band_power(psd, 13.0, 30.0)
    gamma = DataFilter.get_band_power(psd, 30.0, 50.0)

    return {"delta": delta, "theta": theta, "alpha": alpha, "beta": beta, "gamma": gamma}


def compute_metrics(band_powers):
    """Compute SRL-relevant metrics from band powers."""
    alpha = band_powers["alpha"]
    theta = band_powers["theta"]
    beta = band_powers["beta"]

    alpha_theta_ratio = alpha / theta if theta > 0 else 0
    alpha_beta_ratio = alpha / beta if beta > 0 else 0
    total = sum(band_powers.values())
    alpha_relative = alpha / total if total > 0 else 0

    return {
        "alpha_theta_ratio": round(alpha_theta_ratio, 3),
        "alpha_beta_ratio": round(alpha_beta_ratio, 3),
        "alpha_relative_power": round(alpha_relative, 3),
    }


def live_stream(board, eeg_channels, sampling_rate):
    """Print live band powers every 2 seconds."""
    print("\n  LIVE STREAM — Ctrl+C to stop\n")
    print(f"  {'Channel':<20} {'Alpha/Theta':>12} {'Alpha%':>10} {'State':>15}")
    print(f"  {'─' * 60}")

    try:
        while True:
            time.sleep(2)
            data = board.get_current_board_data(sampling_rate * 2)  # 2 seconds of data
            if data.shape[1] < sampling_rate:
                print("  Buffering...")
                continue

            for ch in eeg_channels:
                bp = compute_band_powers(data, sampling_rate, ch)
                metrics = compute_metrics(bp)
                ratio = metrics["alpha_theta_ratio"]
                alpha_pct = metrics["alpha_relative_power"] * 100

                # Simple state classification
                if ratio > 1.5:
                    state = "Focused calm"
                elif ratio > 1.0:
                    state = "Alert"
                elif ratio > 0.6:
                    state = "Transitioning"
                else:
                    state = "Theta dominant"

                ch_name = CHANNEL_NAMES.get(ch, f"Ch {ch}")
                print(f"  {ch_name:<20} {ratio:>12.2f} {alpha_pct:>9.1f}% {state:>15}")
            print()

    except KeyboardInterrupt:
        print("\n  Stream stopped.")


def run_recording(board, eeg_channels, sampling_rate, duration, do_plot=False):
    """Record for specified duration, analyze, and save."""
    print(f"\n  Recording {duration}s of EEG data...")
    print(f"  Sampling rate: {sampling_rate} Hz")
    print(f"  Channels: {len(eeg_channels)} (TP9, AF7, AF8, TP10)")
    print()

    # Progress bar
    for i in range(duration):
        pct = (i + 1) / duration
        bar = "█" * int(pct * 40) + "░" * (40 - int(pct * 40))
        print(f"\r  [{bar}] {i+1}/{duration}s", end="", flush=True)
        time.sleep(1)

    print("\n\n  Recording complete. Analyzing...\n")

    # Get all data
    data = board.get_board_data()
    samples = data.shape[1]
    print(f"  Samples captured: {samples} ({samples/sampling_rate:.1f}s actual)")

    if samples < sampling_rate * 2:
        print("  ERROR: Not enough data captured. Check Muse connection.")
        return None

    # Analyze each channel
    results = {}
    print(f"\n  {'Channel':<20} {'Delta':>8} {'Theta':>8} {'Alpha':>8} {'Beta':>8} {'Gamma':>8} {'A/T Ratio':>10} {'Alpha%':>8}")
    print(f"  {'─' * 82}")

    for ch in eeg_channels:
        bp = compute_band_powers(data, sampling_rate, ch)
        metrics = compute_metrics(bp)
        ch_name = CHANNEL_NAMES.get(ch, f"Ch {ch}")
        results[ch_name] = {**bp, **metrics}

        total = sum(bp.values())
        print(f"  {ch_name:<20} {bp['delta']:>8.1f} {bp['theta']:>8.1f} {bp['alpha']:>8.1f} {bp['beta']:>8.1f} {bp['gamma']:>8.1f} {metrics['alpha_theta_ratio']:>10.2f} {metrics['alpha_relative_power']*100:>7.1f}%")

    # Frontal asymmetry (AF7 vs AF8)
    af7_idx = eeg_channels[1]  # AF7
    af8_idx = eeg_channels[2]  # AF8
    af7_alpha = compute_band_powers(data, sampling_rate, af7_idx)["alpha"]
    af8_alpha = compute_band_powers(data, sampling_rate, af8_idx)["alpha"]

    # Frontal Alpha Asymmetry (FAA): ln(right) - ln(left)
    # Positive = greater left-hemisphere activity (approach motivation)
    # Negative = greater right-hemisphere activity (withdrawal tendency)
    if af7_alpha > 0 and af8_alpha > 0:
        faa = np.log(af8_alpha) - np.log(af7_alpha)
        faa_interp = "approach/engagement" if faa > 0 else "withdrawal/avoidance"
    else:
        faa = 0
        faa_interp = "insufficient data"

    print(f"\n  ═══ SRL Assessment Metrics ═══")
    print(f"  Frontal Alpha Asymmetry (FAA): {faa:.3f} ({faa_interp})")

    # Average alpha/theta across frontal channels
    avg_at = np.mean([results[CHANNEL_NAMES[eeg_channels[1]]]["alpha_theta_ratio"],
                       results[CHANNEL_NAMES[eeg_channels[2]]]["alpha_theta_ratio"]])
    print(f"  Frontal Alpha/Theta Ratio:     {avg_at:.3f}")

    if avg_at > 1.5:
        print(f"  Interpretation:                Dominant alpha — focused calm baseline")
    elif avg_at > 1.0:
        print(f"  Interpretation:                Balanced — alert, moderate regulation")
    elif avg_at > 0.6:
        print(f"  Interpretation:                Theta rising — potential cognitive fatigue or drift")
    else:
        print(f"  Interpretation:                Theta dominant — fatigue, drowsiness, or deep inward focus")

    # Save session data
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "outputs", "eeg-sessions")
    os.makedirs(output_dir, exist_ok=True)

    # Save raw data as CSV
    csv_path = os.path.join(output_dir, f"muse-session-{timestamp}.csv")
    DataFilter.write_file(data, csv_path, "w")
    print(f"\n  Raw data saved: {csv_path}")

    # Save analysis as JSON
    session_report = {
        "timestamp": timestamp,
        "duration_seconds": duration,
        "samples": int(samples),
        "sampling_rate": sampling_rate,
        "device": "Muse 2 (BLED)",
        "channels": CHANNEL_NAMES,
        "band_powers": {k: {bk: round(bv, 3) for bk, bv in v.items()} for k, v in results.items()},
        "frontal_alpha_asymmetry": round(faa, 4),
        "frontal_alpha_asymmetry_interpretation": faa_interp,
        "frontal_alpha_theta_ratio": round(avg_at, 3),
    }
    json_path = os.path.join(output_dir, f"muse-session-{timestamp}.json")
    with open(json_path, "w") as f:
        json.dump(session_report, f, indent=2)
    print(f"  Analysis saved:  {json_path}")

    # Plot if requested
    if do_plot:
        try:
            import matplotlib.pyplot as plt

            fig, axes = plt.subplots(2, 2, figsize=(14, 8))
            fig.suptitle(f"SRL Muse EEG Session — {timestamp}", fontsize=14, fontweight="bold")

            time_axis = np.arange(samples) / sampling_rate

            for i, ch in enumerate(eeg_channels):
                ax = axes[i // 2][i % 2]
                ch_name = CHANNEL_NAMES.get(ch, f"Ch {ch}")
                ax.plot(time_axis, data[ch], linewidth=0.3, color="#22253A", alpha=0.7)
                ax.set_title(ch_name, fontsize=11)
                ax.set_xlabel("Time (s)")
                ax.set_ylabel("uV")
                ax.set_xlim(0, time_axis[-1])

                # Add alpha/theta annotation
                at = results[ch_name]["alpha_theta_ratio"]
                ax.annotate(f"A/T: {at:.2f}", xy=(0.98, 0.95), xycoords="axes fraction",
                           ha="right", va="top", fontsize=9,
                           bbox=dict(boxstyle="round,pad=0.3", facecolor="#5FC89B", alpha=0.3))

            plt.tight_layout()
            plot_path = os.path.join(output_dir, f"muse-session-{timestamp}.png")
            plt.savefig(plot_path, dpi=150)
            print(f"  Plot saved:      {plot_path}")
            plt.show()
        except Exception as e:
            print(f"  Plot error: {e}")

    return session_report


def main():
    parser = argparse.ArgumentParser(description="SRL Muse EEG — BrainFlow Connection")
    parser.add_argument("--duration", type=int, default=60, help="Recording duration in seconds (default: 60)")
    parser.add_argument("--live", action="store_true", help="Live stream mode (Ctrl+C to stop)")
    parser.add_argument("--plot", action="store_true", help="Plot EEG traces after recording")
    parser.add_argument("--board", type=str, default="muse2", choices=["muse2", "muses", "muse2016"],
                        help="Muse model (default: muse2)")
    parser.add_argument("--serial", type=str, default="", help="Serial port (if needed)")
    parser.add_argument("--debug", action="store_true", help="Enable BrainFlow debug logging")
    args = parser.parse_args()

    # Board selection
    board_map = {
        "muse2": BoardIds.MUSE_2_BLED_BOARD,
        "muses": BoardIds.MUSE_S_BLED_BOARD,
        "muse2016": BoardIds.MUSE_2016_BLED_BOARD,
    }
    board_id = board_map[args.board]

    if args.debug:
        BoardShim.enable_board_logger(LogLevels.LEVEL_DEBUG.value)
    else:
        BoardShim.enable_board_logger(LogLevels.LEVEL_OFF.value)

    # Connection params
    params = BrainFlowInputParams()
    if args.serial:
        params.serial_port = args.serial

    # Get board info
    sampling_rate = BoardShim.get_sampling_rate(board_id)
    eeg_channels = BoardShim.get_eeg_channels(board_id)

    print()
    print("  ╔══════════════════════════════════════════╗")
    print("  ║   SRL Muse EEG — BrainFlow Connection    ║")
    print("  ╚══════════════════════════════════════════╝")
    print()
    print(f"  Board:         {args.board.upper()} (BLED / native Bluetooth)")
    print(f"  Board ID:      {board_id}")
    print(f"  Sampling rate: {sampling_rate} Hz")
    print(f"  EEG channels:  {len(eeg_channels)} (TP9, AF7, AF8, TP10)")
    print()

    # Connect
    print("  Connecting to Muse... (make sure it's on and nearby)")
    print("  Tip: Hold power button 2s until LED stabilizes")
    print()

    board = BoardShim(board_id, params)

    try:
        board.prepare_session()
        print("  Session prepared.")

        board.start_stream()
        print("  Stream started.")
        time.sleep(2)  # Let buffer fill

        if args.live:
            live_stream(board, eeg_channels, sampling_rate)
        else:
            run_recording(board, eeg_channels, sampling_rate, args.duration, args.plot)

    except Exception as e:
        print(f"\n  Connection error: {e}")
        print()
        print("  Troubleshooting:")
        print("  1. Is the Muse powered on? (LED should be solid or slow pulse)")
        print("  2. Is Bluetooth enabled on this Mac?")
        print("  3. Is the Muse paired in System Settings > Bluetooth?")
        print("     (Some Muse models need to NOT be paired — try both)")
        print("  4. Try: python3 tools/muse-connect.py --debug")
        print("  5. Try closing any other Muse apps (Mind Monitor, Muse app)")
        print()
        sys.exit(1)

    finally:
        try:
            board.stop_stream()
            board.release_session()
            print("\n  Session released. Muse disconnected cleanly.")
        except:
            pass


if __name__ == "__main__":
    main()
