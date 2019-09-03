#!/usr/bin/env python3
from pathlib import Path
import markdown
import os
import shutil

SRC_DIR = Path('./md')
HTML_DIR = Path('./html')

# Process markdown into html and save it in ./html
for src_file in SRC_DIR.iterdir():
    if src_file.is_dir():
        continue

    print(src_file)
    with open(src_file) as f:
        src_md = f.read()

    src_md = src_md.replace('.md)', '.html)') # fix links

    html_string = markdown.markdown(src_md)
    html_filename = src_file.name.replace(src_file.suffix, '.html')
    html_path = Path(HTML_DIR / html_filename)

    with open(html_path, 'w') as html_file:
        html_file.write(html_string)

