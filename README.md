# The MIT Programs in Digital Humanities Guide for UROPs.

Hosted at [urop guide](https://urop.dhmit.xyz).

This project uses the [11ty static site generator](https://www.11ty.dev/) to generate the static documentation for use by the [Digital Humanities Labs at MIT's](https://digitalhumanities.mit.edu/) UROP programs.

## Development
Development with 11ty is super straightforward! First, using your terminal, navigate to the root directory of the project, and install it by entering the command `npm ci`. 

Once the project is installed, from the root directory, enter the command `npm run dev` into the terminal and visit `localhost:8080` to view a development draft of the website with hot reloading. Enter the command `npm run build` to generate the full website build.

Add new pages in the `views` directory using any HTML templating language you wish (`.html`, `.nkj`, `.liquid`, etc.). All pages can contain optional `front matter`, indicated by the use of dashes at the top of the page:

```
layouts: layouts/base
meta_title: 'Some HTML <title> content`
title: `The page’s <h1> content`
```

For now, the deployment strategy is to check in the `docs` directory and let GitHub's default static-site deployment handle hosting the pages generated in that directory. In the future, we should automate this out via GitHub Actions and remove the `docs` directory from the repo. When you've finalized changes to the repo, make sure to run `npm run build` locally and check those changes in.
