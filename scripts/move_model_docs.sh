#!/bin/bash

process_file() {
  echo "Processing $1"
  if [[ "$1" == *.md ]]; then
    # It's a markdown file
    if [ -f "$1" ]; then
      echo "Moving $1 to docs/reference/"
    mv "$1" docs/reference/
    # Update .openapi-generator/FILES to reflect the new location
    sed -i '' "s|$1|docs/reference/$(basename "$1")|" .openapi-generator/FILES
    fi
  fi
}

# Get doc files
for f in docs/*.md; do
  [ -e "$f" ] || continue
  process_file "$f"
done
