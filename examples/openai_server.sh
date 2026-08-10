#!/usr/bin/env bash
set -euo pipefail

# Same runtime as run_qwen35.py, kept resident and served over HTTP.
python3 scripts/serve_openai.py \
  --mlx /path/to/mlx-Qwen3.5-35B-A3B-4bit \
  --experts /path/to/packed_experts \
  --slot-bank 64 \
  --slot-bank-native \
  --prefetch-temporal \
  --cache-io-split 4 \
  --k 4 \
  --host 127.0.0.1 \
  --port 8080

# Then, from another shell:
#
#   curl http://127.0.0.1:8080/v1/chat/completions \
#     -H 'Content-Type: application/json' \
#     -d '{"messages": [{"role": "user", "content": "What is Apple Neural Engine?"}],
#          "max_tokens": 120, "stream": true}'
