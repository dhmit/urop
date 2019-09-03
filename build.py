#!/usr/bin/env python3
from pathlib import Path
import os
import shutil

import jinja2

TEMPLATE_DIR = Path('./templates')
SRC_IMG_DIR = Path('./md/images')
BUILD_DIR = Path('./docs')
BUILD_IMG_DIR = Path(BUILD_DIR / 'images')

# Clean and remake build dir
if os.path.exists(BUILD_DIR):
    shutil.rmtree(BUILD_DIR)
os.makedirs(BUILD_DIR)

# Copy images from src to build
shutil.copytree(SRC_IMG_DIR, BUILD_IMG_DIR)

# Write out CNAME
with open(Path(TEMPLATE_DIR / 'CNAME'), 'w') as f:
    f.write('urop.dhmit.xyz')

# setup Jinja2 template loader and environment
template_loader = jinja2.FileSystemLoader(searchpath=str(TEMPLATE_DIR))
template_env = jinja2.Environment(loader=template_loader)

# Process markdown into html and save it in build
for template in TEMPLATE_DIR.iterdir():
    print('Building ', template)
    if template.is_dir() or template.name == 'base.html':
        continue

    template = template_env.get_template(template.name)
    rendered_template = template.render()

    build_filename = template.name
    build_path = Path(BUILD_DIR / build_filename)

    with open(build_path, 'w') as build_file:
        build_file.write(rendered_template)

