#!/usr/bin/env python3
from pathlib import Path
import markdown
import os
import shutil

SRC_DIR = Path('./src')
SRC_IMG_DIR = Path(SRC_DIR / 'images')
BUILD_DIR = Path('./docs')
BUILD_IMG_DIR = Path(BUILD_DIR / 'images')

TEMPLATE = Path('./template.html')
CONTENT_TAG = '{{ content }}'

# Clean and remake build dir
if os.path.exists(BUILD_DIR):
    shutil.rmtree(BUILD_DIR)
os.makedirs(BUILD_DIR)

# Copy images from src to build
shutil.copytree(SRC_IMG_DIR, BUILD_IMG_DIR)

# Load template
with open(TEMPLATE) as f:
    template_html = f.read()

# Process markdown into html and save it in build
for src_file in SRC_DIR.iterdir():
    if src_file.is_dir():
        continue

    print(src_file)
    with open(src_file) as f:
        src_md = f.read()

    content_html = markdown.markdown(src_md)
    out_html = template_html.replace(CONTENT_TAG, content_html)

    html_filename = src_file.name.replace(src_file.suffix, '.html')
    html_path = Path(BUILD_DIR / html_filename)

    with open(html_path, 'w') as html_file:
        html_file.write(out_html)

