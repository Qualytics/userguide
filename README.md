# Qualytics User Guide Repository

This repository contains the documentation for the Qualytics platform, built using [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

## Getting Started

### Requirements

This project requires the following tools:

- [Python 3.13+](https://www.python.org/)
- [MkDocs](https://www.mkdocs.org/)
- [pre-commit](https://pre-commit.com/)
- [typos](https://github.com/crate-ci/typos)
- [mkdocs-print-site-plugin](https://github.com/timvink/mkdocs-print-site-plugin)
- [VS Code](https://code.visualstudio.com/) with the [Run on Save](https://marketplace.visualstudio.com/items?itemName=emeraldwalk.RunOnSave) extension (recommended)

### Running the Project Locally

To preview the documentation locally:

```bash
mkdocs serve
```

> [!NOTE]
> By default, the documentation will be served at `http://localhost:8000`.

> [!TIP]
> To run it on a custom port (e.g., 8080):
>
> ```bash
> mkdocs serve -a localhost:8080
> ```

### Enabling PDF Export

To enable PDF export via the print-site plugin:

1. Open the mkdocs.yml file.
2. Set the print-site plugin to enabled.
3. Run mkdocs build or mkdocs serve.

## Setting Up the Local Environment

### Create a Virtual Environment

Create a Python virtual environment:

```bash
python3 -m venv <your_env_name>
```

> [!NOTE]
> Replace `<your_env_name>` with your desired virtual environment folder name.

### Activate the Virtual Environment

Use the appropriate command based on your operating system and shell:

| Platform | Shell      | Command                           |
| -------- | ---------- | --------------------------------- |
| POSIX    | bash/zsh   | `source <venv>/bin/activate`      |
|          | fish       | `source <venv>/bin/activate.fish` |
|          | csh/tcsh   | `source <venv>/bin/activate.csh`  |
|          | pwsh       | `<venv>/bin/Activate.ps1`         |
| Windows  | cmd.exe    | `<venv>\Scripts\activate.bat`     |
|          | PowerShell | `<venv>\Scripts\Activate.ps1`     |

> [!NOTE]
> Replace `<venv>` with the path to your virtual environment folder.

### Upgrade pip

```bash
python -m pip install --upgrade pip
```

### Install Project Dependencies

```bash
pip install -r requirements.txt
```

### Pre-Commit Setup

This repository uses [pre-commit](https://pre-commit.com/) to automatically check for spelling errors using [typos](https://github.com/crate-ci/typos).

#### Install Pre-Commit

```bash
pip install pre-commit
```

#### Install Pre-Commit Hooks

```bash
pre-commit install
```

#### Run Typos Manually

To run the pre-commit checks manually:

```bash
pre-commit run --all-files
```
