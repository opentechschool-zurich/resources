import argparse
import re

argparser = argparse.ArgumentParser()
argparser.add_argument('filename')
args = argparser.parse_args()
with open(args.filename) as file:
    markdown = file.read()

toc_start_marker = '<!-- toc -->'
toc_end_marker = '<!-- /toc -->'

toc_start = markdown.find(toc_start_marker)
toc_end = markdown.find(toc_end_marker)

# print(markdown[toc_start + len(toc_start_marker):toc_end])

headings = re.findall(r'^#(#+) (.+)$', markdown, re.MULTILINE)

def getHeadingsWithId(headings):
    result = []
    for heading in headings:
        id = re.sub(r'[^\w\s-]', '', heading[1]).strip().lower()
        id = re.sub(r'\s+', '-', id)
        result.append((heading[0], heading[1], id))
    return result

toc = []
for heading in getHeadingsWithId(headings):
    toc.append('{}- [{}](#{})'.format('  ' * (len(heading[0]) - 1), heading[1], heading[2]))
# print(toc)

with open(args.filename, 'w') as file:
    file.write(
        markdown[0:toc_start + len(toc_start_marker) + 1] +
        '\n'.join(toc) +
        markdown[toc_end - 1:]
    )
