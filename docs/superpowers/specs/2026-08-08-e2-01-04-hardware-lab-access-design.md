# E2-01-04 Hardware Lab Access Design

## Goal

Add a bilingual Wiki guide for gaining access to and working in the E2-01-04 Control & Mechatronics hardware laboratory. Keep the existing COM2-0106 access guide unchanged.

The new guide must let members read the application requirements in the browser and download sanitized working copies of the required forms without publishing personal information.

## Source Material

The guide is based on:

- A Control & Mechatronics Lab registration email containing the required training and application sequence.
- The Control Group user registration form.
- The E2-01-04 activity-based risk assessment for robot and dexterous-hand work.

The source email itself will not be published. Its operational content will be rewritten as searchable Wiki content. The two forms will be published only after sanitization.

## Information Architecture

Create a new Chinese page and a matching English page under Onboarding. Add a distinct navigation entry for E2-01-04 hardware lab access while preserving the existing COM2-0106 entry.

Each page will contain:

1. Purpose and applicable location.
2. Prerequisites.
3. Required safety training, including course code, title, platform, audience, and available links.
4. The registration sequence from training through access activation.
5. Required submission materials and the laboratory functional mailbox.
6. A browser-readable overview of the user registration form.
7. A browser-readable risk assessment reference retaining the experiment steps, hazards, consequences, risk ratings, and controls.
8. Direct download links for the sanitized form files.
9. Verification, troubleshooting, maintainer, and last-verified information.

Long risk-assessment material may use collapsible sections or tables so the operational procedure remains easy to scan.

## Attachments

Store sanitized attachments below `docs/assets/forms/e2-01-04/` so MkDocs copies them into the built site and standard links work on GitHub Pages.

- Preserve the user registration form as a `.doc` download.
- Preserve the risk assessment as a `.docx` download.
- Use the Wiki pages, rather than duplicated PDF exports, as the browser preview.

The published filenames will identify them as sanitized copies. The page will explain that users must replace placeholders and review the forms before submission.

## Redaction Rules

Remove or replace all person-specific content before copying attachments into the repository:

- Names and declarations containing names.
- Matriculation or employee identifiers.
- Personal phone numbers and email addresses.
- Emergency contact details.
- Signatures and signature images.
- Person-specific completion, review, attachment-period, approval, and deadline dates.
- Names in `Action By`, conducted-by, approved-by, and presence fields.
- Document metadata or embedded content that identifies the original applicant.

Use unambiguous placeholders such as `<APPLICANT_NAME>`, `<MATRIC_OR_STAFF_ID>`, `<DATE>`, and `<SUPERVISOR_NAME>` where the file format permits. Fixed-length blank replacements are acceptable where the legacy `.doc` format cannot safely accommodate longer placeholder text.

Retain the non-personal operational material:

- Location E2-01-04 and laboratory identity.
- Robot, teleoperation, workstation, and dexterous-hand activities.
- Hazards, consequences, risk scores, controls, and the risk matrix.
- General laboratory rules.
- Training codes and course titles.
- Official training links and the laboratory functional mailbox needed for submission.

Do not publish the original source files. After sanitization, scan both the rendered Wiki content and binary attachment contents for known identifiers from the source material.

## Content Behavior

Members can follow one of two paths from the same page:

- Read the training, submission process, form fields, and risk reference directly in the browser.
- Download the sanitized editable forms, replace placeholders, complete missing fields, export both completed forms to PDF, and submit them with a photo to the laboratory functional mailbox.

The page will distinguish staff-only courses from courses available to all lab users. It will also state that the safety orientation invitation and access activation notification arrive by email.

## Error Handling And Safety Notes

- If a training course cannot be found, verify the course code in the relevant learning platform and contact the laboratory administrator.
- If an attachment does not open in the browser, download it and use a compatible office application.
- Warn users not to upload completed personal forms back to the public Wiki repository.
- Treat the risk assessment as a reference, not automatic approval for every project. Users must review project-specific hazards and controls with their supervisor or laboratory staff.

## Validation

Before completion:

1. Confirm Chinese and English navigation and content structures match.
2. Verify every training and attachment link resolves in the built site.
3. Confirm the original COM2-0106 page remains unchanged.
4. Search the repository and attachment contents for all known source identifiers.
5. Inspect the sanitized forms to confirm useful operational content remains.
6. Run `mkdocs build --strict`.

## Out Of Scope

- Publishing the Outlook email PDF.
- Publishing completed or signed application forms.
- Replacing official approval or laboratory-specific safety review.
- Adding authentication or external document storage.

