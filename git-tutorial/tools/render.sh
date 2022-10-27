#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

if [[ $# -lt 1 ]]; then
    echo "Usage: $0 file.md"
    exit
fi

filename=$1

extension="${filename##*.}"

if [[ "$extension" != "md" ]]; then
    echo "Only .md files are supported"
    exit
fi

base_filename=${filename%.*}
echo $base_filename

pandoc "$filename" -o "$base_filename.html"
pandoc "$base_filename.html" -f gfm -t html5 -o "render/$base_filename.pdf" --highlight-style pygments --pdf-engine=wkhtmltopdf --css=tools/md-to-html.css --pdf-engine-opt=--enable-local-file-access
rm "$base_filename.html"
