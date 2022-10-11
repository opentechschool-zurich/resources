pandoc introduction-to-git.md -o introduction-to-git.html
pandoc introduction-to-git.html -f gfm -t html5 -o render/introduction-to-git.pdf --highlight-style pygments --css=tools/md-to-html.css --pdf-engine-opt=--enable-local-file-access
rm introduction-to-git.html