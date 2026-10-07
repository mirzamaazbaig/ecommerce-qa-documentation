# D5: A non-numeric product id returns a server error

| Field | Value |
|---|---|
| Severity | Low |
| Priority | Low |
| Area | Products / API |
| Environment | Application branch under test, Node 22, PostgreSQL 16, Chromium |
| Found by | Automated test written to assert the correct behaviour |
| Status | Fixed and verified |

## Steps to reproduce
1. `GET /api/products/abc`.

## Expected result
`400 Invalid product id`.

## Actual result
`500`; the database rejected the cast of `abc` to integer and the error surfaced.

## Impact
A client mistake looks like an outage, floods error logs and can leak details about the database.

## Root cause
The id went into the query unchecked.

## Fix
Ids are validated as positive integers within the PostgreSQL range before any query, for get, update and delete.

## Verification
`TC_API_PROD_013` (six invalid ids, including a SQL fragment) and `014`. The same tests were run against the code before the fix to prove they fail there.

Source: the application repository's `docs/KNOWN_DEFECTS.md`, entry D5.
