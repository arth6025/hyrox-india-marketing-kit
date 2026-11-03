#!/usr/bin/env bash
# Build dist/sloosh-skills-<version>.zip for upload to Claude (Customize → Plugins → Upload plugin).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
VERSION=$(python3 -c "import json;print(json.load(open('.claude-plugin/plugin.json'))['version'])")
python3 scripts/validate_skills.py --evals
python3 scripts/build_registry.py
python3 scripts/build_capability_map.py
mkdir -p dist
OUT="dist/sloosh-skills-${VERSION}.zip"
rm -f "$OUT"
zip -qr "$OUT" . \
  -x "dist/*" ".git/*" "*/node_modules/*" "*/__pycache__/*" "*.pyc" ".DS_Store" "*/.DS_Store"

echo "wrote $OUT ($(du -h "$OUT" | cut -f1))"
