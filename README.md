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

## GitHub Pages deployment

The repository deploys automatically from `main` through
`.github/workflows/deploy.yml`.

Repository administrators should set **Settings → Pages → Source** to
**GitHub Actions**. The published site is
`https://lv-robotics-lab.github.io/lab-wiki/`.

## Public-test warning

Do not commit real internal addresses, credentials, member records, unpublished research information, or administrative documents during the public testing stage.
