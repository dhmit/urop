# The MIT Programs in Digital Humanities Guide for UROPs.

Hosted at [urop guide](https://urop.dhmit.xyz).

This project uses the [11ty static site generator](https://www.11ty.dev/), [GitHub Actions](https://github.com/features/actions), and []() to generate the static documentation for use by the [Digital Humanities Labs at MIT's](https://digitalhumanities.mit.edu/) UROP programs.

## Development
Development with 11ty is super straightforward! At the root directory, enter the command `npm run dev` into the terminal and visit `localhost:8080` to view a development draft of the website with hot reloading. Enter the command `npm run build` to generate the full website build.

Add new pages in the `views` directory using any HTML templating language you wish (`.html`, `.nkj`, `.liquid`, etc.). All pages can contain optional `front matter`, indicated by the use of dashes at the top of the page:

```
layouts: layouts/base
meta_title: 'Some HTML <title> content`
title: `The page’s <h1> content`
```

All pages in the `views` directory will be compiled, built, and hosted at [https://urop.dhmit.xyz](https://urop.dhmit.xyz) automatically when an open PR is merged into the main branch.
