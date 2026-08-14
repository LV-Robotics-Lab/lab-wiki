# How to Contribute

## Recommended workflow

1. Create a branch from `main`.
2. Update the corresponding Chinese and English Markdown files.
3. Run `mkdocs serve` locally to review the result.
4. Open a pull request.
5. Merge after maintainer review.

## File naming

- Default Chinese page: `page.md`
- English page: `page.en.md`
- Use lowercase names and hyphens

## Local preview

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

## Maintenance

- **Maintainer:** Wiki Team
- **Last verified:** 2026-08-14
