# Qualytics Userguide Repo

We use [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/getting-started/) to build our guide.

Once setup - simply run `mkdocs serve` locally for a live preview. Another option is running `mkdocs serve -a localhost:8080` in case you want to specify a different port, by default, the project will run at the port `8000`.


## Rendering as a single PDF

We are using: https://github.com/orzih/mkdocs-with-pdf which requires installation of [WeasyPrint](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation)

Enable the PDF plugin in mkdocs.yml then run mkdocs build
