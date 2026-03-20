#!/usr/bin/env python3
"""
SRL Biomedical Query Tool — Query BioMistral or other HuggingFace medical LLMs.

Usage:
  python3 tools/biomedical-query.py "What are the mechanisms of vagal tone improvement through slow breathing?"
  python3 tools/biomedical-query.py --model med42 "Describe HRV biofeedback evidence for CRNA burnout"
  python3 tools/biomedical-query.py --model biomistral-clinical "Interoceptive accuracy measurement methods"

Environment:
  HUGGINGFACE_TOKEN — your HF API token (set via `export` or .env)

Models available:
  biomistral         — BioMistral/BioMistral-7B (default, PubMed-trained, fast)
  biomistral-clinical — Incredible88/BioMistral-Clinical-7B (clinical focus)
  med42              — m42-health/med42-70b (70B, USMLE 72%, slower)
  medalpaca          — medalpaca/medalpaca-13b (13B, instruction-tuned)
  biomedicine        — AdaptLLM/medicine-LLM (7B, domain-adapted)
"""

import argparse
import json
import os
import sys
import urllib.request
import urllib.error

MODELS = {
    "qwen-large": "Qwen/Qwen3-235B-A22B",
    "qwen": "Qwen/Qwen3-32B",
    "qwen-small": "Qwen/Qwen3-8B",
    "deepseek-r1": "deepseek-ai/DeepSeek-R1",
    "deepseek-v3": "deepseek-ai/DeepSeek-V3.2",
    "llama-70b": "meta-llama/Llama-3.3-70B-Instruct",
    "llama-8b": "meta-llama/Llama-3.1-8B-Instruct",
}

DEFAULT_MODEL = "qwen"

SYSTEM_CONTEXT = """You are a biomedical research assistant for Somnistics Research Labs.
Focus areas: autonomic regulation, HRV biofeedback, interoception, breathwork mechanisms,
CRNA clinical performance, stress physiology, vagal tone, and clinician durability.
Cite specific studies when possible. Be precise and evidence-based."""


def query_huggingface(prompt: str, model_id: str, token: str, max_tokens: int = 1024) -> str:
    """Query HuggingFace via OpenAI-compatible chat completions endpoint."""
    url = "https://router.huggingface.co/v1/chat/completions"

    payload = {
        "model": model_id,
        "messages": [
            {"role": "system", "content": SYSTEM_CONTEXT},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": max_tokens,
        "temperature": 0.3,
        "top_p": 0.9,
    }

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "User-Agent": "SRL-Vigil/1.0",
    }

    req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers=headers)

    try:
        with urllib.request.urlopen(req, timeout=120) as response:
            result = json.loads(response.read().decode())

            if "choices" in result and len(result["choices"]) > 0:
                return result["choices"][0]["message"]["content"]
            elif "error" in result:
                return f"Error: {result['error']}"
            return json.dumps(result, indent=2)

    except urllib.error.HTTPError as e:
        body = e.read().decode()
        try:
            err = json.loads(body)
            if "estimated_time" in err:
                return f"Model loading... estimated wait: {err['estimated_time']:.0f}s. Retry in a minute."
            return f"HTTP {e.code}: {err.get('error', body)}"
        except:
            return f"HTTP {e.code}: {body}"
    except urllib.error.URLError as e:
        return f"Connection error: {e.reason}"
    except Exception as e:
        return f"Error: {e}"


def main():
    parser = argparse.ArgumentParser(description="Query biomedical LLMs via HuggingFace")
    parser.add_argument("prompt", nargs="?", help="The biomedical question to ask")
    parser.add_argument("--model", "-m", default=DEFAULT_MODEL,
                        choices=list(MODELS.keys()),
                        help=f"Model to use (default: {DEFAULT_MODEL})")
    parser.add_argument("--max-tokens", "-t", type=int, default=1024,
                        help="Max tokens to generate (default: 1024)")
    parser.add_argument("--list-models", "-l", action="store_true",
                        help="List available models")
    parser.add_argument("--json", "-j", action="store_true",
                        help="Output raw JSON response")

    args = parser.parse_args()

    if args.list_models:
        print("Available biomedical models:")
        for key, model_id in MODELS.items():
            default = " (default)" if key == DEFAULT_MODEL else ""
            print(f"  {key:25s} → {model_id}{default}")
        return

    if not args.prompt:
        # Read from stdin if no prompt argument
        if not sys.stdin.isatty():
            args.prompt = sys.stdin.read().strip()
        else:
            parser.error("Please provide a prompt or pipe input via stdin")

    token = os.environ.get("HUGGINGFACE_TOKEN") or os.environ.get("HF_TOKEN")
    if not token:
        # Try reading from .env file
        env_file = os.path.join(os.path.dirname(__file__), "..", ".env")
        if os.path.exists(env_file):
            with open(env_file) as f:
                for line in f:
                    if line.startswith("HUGGINGFACE_TOKEN=") or line.startswith("HF_TOKEN="):
                        token = line.split("=", 1)[1].strip().strip('"').strip("'")
                        break

    if not token:
        print("Error: No HuggingFace token found.")
        print("Set HUGGINGFACE_TOKEN or HF_TOKEN environment variable.")
        print("Get a free token at: https://huggingface.co/settings/tokens")
        sys.exit(1)

    model_id = MODELS[args.model]

    if not args.json:
        print(f"Model: {model_id}")
        print(f"Query: {args.prompt[:100]}{'...' if len(args.prompt) > 100 else ''}")
        print("---")

    response = query_huggingface(args.prompt, model_id, token, args.max_tokens)

    if args.json:
        print(json.dumps({"model": model_id, "prompt": args.prompt, "response": response}, indent=2))
    else:
        print(response)


if __name__ == "__main__":
    main()
