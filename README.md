# Lab Wiki Starter

A bilingual Material for MkDocs starter for a laboratory wiki. Chinese is the default language and English is available through the language selector.

## Local preview

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Open `http://127.0.0.1:8000`.

## GitHub Pages setup

1. Push this repository to GitHub using the `main` branch.
2. Open **Settings → Pages**.
3. Set **Source** to **GitHub Actions**.
4. Push a commit or run the workflow manually.

Before publishing, replace `example` in `mkdocs.yml` with your GitHub username and repository URL.

## Public-test warning

Do not commit real internal addresses, credentials, member records, unpublished research information, or administrative documents during the public testing stage.
