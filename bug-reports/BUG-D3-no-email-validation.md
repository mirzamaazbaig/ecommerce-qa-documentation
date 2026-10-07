# D3: Registration accepts any text as an email address

| Field | Value |
|---|---|
| Severity | Medium |
| Priority | Medium |
| Area | Authentication / API |
| Environment | Application branch under test, Node 22, PostgreSQL 16, Chromium |
| Found by | Automated test written to assert the correct behaviour |
| Status | Fixed and verified |

## Steps to reproduce
1. `POST /api/auth/register` with `{"email": "not-an-email", "password": "TestPass123!"}`.

## Expected result
`400` with a validation message; nothing stored.

## Actual result
`201 Created`; an account with the email `not-an-email` exists.

## Impact
Accounts that can never receive mail; garbage in the user table; no way to recover a password later.

## Root cause
No format check on the email.

## Fix
The email must be text of at most 255 characters matching `local@domain.tld`; otherwise 400.

## Verification
`TC_API_AUTH_009` (a unique malformed email per run, and a check that nothing was stored). The same tests were run against the code before the fix to prove they fail there.

Source: the application repository's `docs/KNOWN_DEFECTS.md`, entry D3.
