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

To preview the documentation locally

1. Activate the [virtual environment](#setting-up-the-local-environment)
2. Run the following command:

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

This repository uses [pre-commit](https://pre-commit.com/) hooks to catch issues before they reach the repository. Two hooks are configured:

1. **typos** - Spell checking across all documentation files using [typos](https://github.com/crate-ci/typos). Custom word allowances are defined in `.typos.toml`.
2. **mkdocs-warnings** - Runs `mkdocs build` and reports any `WARNING` lines (broken links, missing nav entries, etc.). This hook reports warnings without failing the build to avoid blocking commits on acceptable warnings.

#### Install Pre-Commit

```bash
pip install pre-commit
```

#### Install Pre-Commit Hooks

```bash
pre-commit install
```

#### Run Hooks Manually

To run all pre-commit checks manually:

```bash
pre-commit run --all-files
```

#### MkDocs Validation

The `mkdocs.yml` file includes a `validation` section that controls which link and reference issues produce warnings during the build. This can be expanded to catch more issues:

```yaml
# Example: expanded validation config
validation:
  nav:
    omitted_files: info
    absolute_links: warn
  links:
    anchors: warn
    absolute_links: warn
    unrecognized_links: warn
```

To enforce stricter checks, the hook can be updated to use `mkdocs build --strict` (turns warnings into errors) or to filter out known acceptable warnings while failing on the rest.

## Run on Save (Opctional)

If you are using Visual Studio Code, it's recommended to install the [Run on Save](https://marketplace.visualstudio.com/items?itemName=emeraldwalk.RunOnSave) extension.

With this extension, every time you save a file in the project, it automatically executes `Typos` to check for misspelled words throughout the codebase. The results will be shown in the Output panel under the `Run On Save` section.

To configure it, add the following snippet to your `.vscode/settings.json`:

```json
{
  "emeraldwalk.runonsave": {
    "commands": [
      {
        "match": ".*",
        "cmd": "pre-commit run --all-files"
      }
    ]
  }
}
```

> [!NOTE]
> Make sure `pre-commit` is installed and the virtual environment is activated in your terminal when using this setup.
