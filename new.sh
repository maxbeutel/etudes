etudes_file="$1"

selected=$(grep '^\* ' "$etudes_file" | grep -v TODO | sort -R | head -n 5)
dir=$(date +%Y%m%d)

mkdir -p "$dir"

echo "$selected" > "$dir/selected.txt"
echo "$selected"
