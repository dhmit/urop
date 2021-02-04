#!/usr/bin/env python3
from pathlib import Path
import markdown
import os
import shutil

SRC_DIR = Path('./md')
HTML_DIR = Path('./html')

macro = '''
{% macro row(text, image) -%}
    <hr class="d-lg-none">
    <div class="row">
        <div class="col-lg-4">
            {{ text }}
        </div>
        <div class="col-lg-8">
            {{ image }}
        </div>
    </div>
{%- endmacro %}
'''

# Process markdown into html and save it in ./html
for src_file in SRC_DIR.iterdir():
    if str(src_file) != 'md/lang_learn.md':
        continue

    if src_file.is_dir() or src_file.name.endswith('swp'):
        continue

    print(src_file)
    with open(src_file, encoding='utf-8') as f:
        src_md = f.read()

    src_md = src_md.replace('.md)', '.html)') # fix links

    html_string = markdown.markdown(src_md)

    html_string = html_string.replace('<h1>', '{% block title %}') # h1 to title block
    html_string = html_string.replace('</h1>',
                                      '{% endblock %}\n{% block content %}')

    html_string = html_string.replace('<img', '<img class="img-fluid"') # add img-fluid class
    html_string = "{% extends 'base.html' %}\n" + macro + "\n" + html_string + '\n{% endblock %}'

    # Split up the html string by newline and only extract the part that is inside the {% block content %}
    lines_before_content = 16
    html_parts = html_string.split("\n")
    content = html_parts[lines_before_content:-1]

    # Rebuild the html string by using the macro where it is necessary and escaping quotes and backslashes
    # so that build.py runs properly
    html_string = '\n'.join(html_parts[:lines_before_content]) + '\n\n'
    cur_row = ''
    for line in content:
        if line[:2] == '<h':
            # when there is a header tag, we do not need bootstrap rows
            cur_row += line.replace("'", "&#x27;").replace('\\', '\\\\') + '\n'
            html_string += cur_row
            cur_row = ''
        elif '<img' in line:
            # when there is an image, we call the macro with the text and image tags
            img_start = line.index('<img')
            img_end = line.index('/>') + 2
            image = '<p>' + line[img_start: img_end] + '</p>'
            html_string += '{{ row(\'' + cur_row + '\', \'' + image + '\') }}\n'
            cur_row = ''
        elif line[:3] == '<p>':
            # when there is just a paragraph, we add it to the the text we have so far
            cur_row += line.replace("'", "&#x27;").replace('\\', '\\\\') + '\n'

    # Add in the last row if it wasn't added already and add the {% endblock %} at the end
    if cur_row != '':
        html_string += cur_row
    html_string += html_parts[-1]

    html_filename = src_file.name.replace(src_file.suffix, '.html')
    html_path = Path(HTML_DIR / html_filename)

    with open(html_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_string)
