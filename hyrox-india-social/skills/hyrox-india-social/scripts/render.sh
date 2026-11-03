#!/usr/bin/env bash
# Render a HYROX post HTML to PNG at its exact canvas size.
#   render.sh <post.html> [out.png]
# The canvas size is read from <body data-w="1080" data-h="1350">.


set -euo pipefail

in="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
out="${2:-${in%.html}.png}"

find_chrome() {
  local c
  for c in \
    "${CHROME:-}" \
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
    "/Applications/Chromium.app/Contents/MacOS/Chromium" \
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge" \
    "$(command -v google-chrome || true)" "$(command -v chromium || true)"; do
    [ -n "$c" ] && [ -x "$c" ] && { echo "$c"; return; }
  done
  # Playwright's bundled Chromium (path contains spaces, so use find)
  c="$(find "$HOME/Library/Caches/ms-playwright" "$HOME/.cache/ms-playwright" -maxdepth 7 -type f -perm +111 \
        \( -name 'Google Chrome for Testing' -o -name 'Chromium' -o -name chrome \) 2>/dev/null | sort -r | head -1)"
  [ -n "$c" ] && { echo "$c"; return; }
  echo "No Chrome/Chromium found. Install Google Chrome or run: npx playwright install chromium" >&2
  exit 1
}
CHROME_BIN="$(find_chrome)"

w=$(grep -o 'data-w="[0-9]*"' "$in" | head -1 | grep -o '[0-9]*')
h=$(grep -o 'data-h="[0-9]*"' "$in" | head -1 | grep -o '[0-9]*')

"$CHROME_BIN" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 \
  --allow-file-access-from-files --virtual-time-budget=6000 \
  --window-size="$w,$h" --screenshot="$out" "file://$in" >/dev/null 2>&1 || true
[ -s "$out" ] || { echo "Render failed: $in" >&2; exit 1; }
echo "$out"

# Locked text sizes: the page marks any text that still overflows its box at the smallest allowed size
over=$("$CHROME_BIN" --headless=new --disable-gpu --allow-file-access-from-files --virtual-time-budget=6000 \
  --window-size="$w,$h" --dump-dom "file://$in" 2>/dev/null | grep -o 'data-overflow="[^"]*"' | sed 's/data-overflow=//' | tr -d '"' | sort -u | tr '\n' ' ' || true)
[ -n "$over" ] && echo "  ⚠ COPY TOO LONG in: ${over}- shorten the copy (HYROX templates keep fixed text sizes)."
exit 0
