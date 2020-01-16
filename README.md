The MIT Programs in Digital Humanities Guide for UROPs.

Hosted at [urop guide](https://urop.dhmit.xyz).

A quick primer on how this all works:

* we draft content as md files in ./md
* md_to_html.py generates html from these md files, and puts it in html/
* when ready, move an html file from html/ to templates/
* build.py runs jinja on the template and outputs the final result into docs
* docs is what gets hosted by github pages
