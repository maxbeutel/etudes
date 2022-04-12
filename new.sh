#!/bin/bash

etudes_file="$1"
num="$2"

selected=$(grep '^\* ' "$etudes_file" | grep -v TODO | sort -R | head -n "$num")
dir=$(date +%Y%m%d)

mkdir -p "$dir"

echo "$selected" > "$dir/selected.txt"
echo "$selected"
