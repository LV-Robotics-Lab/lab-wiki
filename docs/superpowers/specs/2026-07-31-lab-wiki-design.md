# Lab Wiki Starter Design

## Goal

Create a public test version of a bilingual laboratory wiki with a CSDIY-style documentation UI, Chinese as the default language, and English pages with matching structure.

## Scope

The first version contains a dashboard-style documentation homepage, onboarding pages, administrative procedure pages, and a contribution guide. It uses demonstration content only and excludes access control until Cloudflare is added later.

## Architecture

Markdown files are built by Material for MkDocs. `mkdocs-static-i18n` uses suffix-based translations: Chinese pages use `.md` and English pages use `.en.md`. GitHub Actions builds the static site and deploys it to GitHub Pages.

## Constraints

- Default language: Chinese.
- Secondary language: English.
- Chinese and English navigation structures correspond.
- Visual style: documentation-first, similar to CSDIY.
- First-version content: onboarding and administration.
- Public testing must contain no sensitive laboratory information.
