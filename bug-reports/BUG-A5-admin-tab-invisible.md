# A5: Inactive admin dashboard tab is practically invisible (contrast 1.1:1)

| Field | Value |
|---|---|
| Severity | Medium |
| Priority | Serious (accessibility) |
| Area | Admin dashboard / UI |
| Environment | Application branch under test, Node 22, PostgreSQL 16, Chromium |
| Found by | Automated test written to assert the correct behaviour |
| Status | Fixed and verified |

## Steps to reproduce
1. Sign in as an admin.
2. Open the dashboard.
3. Look at the inactive tab (Orders or Products).

## Expected result
Inactive tab text is readable (contrast at least 4.5:1).

## Actual result
White text on the light grey page background; contrast 1.1:1. The axe-core `color-contrast` rule fails.

## Impact
Administrators cannot see how to switch between Products and Orders; fails WCAG 2.1 AA (1.4.3).

## Root cause
A rule meant for the dark navbar, `.nav-link { color: white !important }`, applied to every `.nav-link` in the app.

## Fix
The rule was scoped to `.navbar .nav-link`; the inactive tab uses a darker blue.

## Verification
`TC_A11Y_012` and `TC_A11Y_014` (axe scan of the admin dashboard) fail before the fix and pass after it. The same tests were run against the code before the fix to prove they fail there.

Source: the application repository's `docs/KNOWN_DEFECTS.md`, entry A5.
