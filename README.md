# Qualytics Userguide Repo

We use [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/getting-started/) to build our guide.

Once setup - simply run `mkdocs serve` locally for a live preview. Another option is running `mkdocs serve -a localhost:8080` in case you want to specify a different port, by default, the project will run at the port `8000`.


## Rendering as a single PDF

We are using the [mkdocs-print-site-plugin](https://github.com/timvink/mkdocs-print-site-plugin) plugin to add a 
print page that combines all the docs, allowing for easy export to PDF and standalone HTML.
