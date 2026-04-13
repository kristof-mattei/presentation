#!/usr/bin/env bash
set -e

cd "$(dirname "$0")"

echo "Rendering charts..."
for f in charts/*.mmd; do
  npx -y @mermaid-js/mermaid-cli -i "$f" -o "${f%.mmd}.png" -b transparent --width 900 --height 500 &
done
wait

echo "Building slides..."
npx @marp-team/marp-cli slides.md -o slides.html --html

echo "Done: slides.html"
