# Product risk register

Score = likelihood x impact on a 1 to 3 scale (1 low, 3 high). Likelihood is a judgement from the code and from what the first test runs found. Test effort follows the score.

| ID | Risk | L | I | Score | Mitigation (tests) | Requirements |
|---|---|---|---|---|---|---|
| R1 | Orders oversell stock or charge the wrong price | 3 | 3 | **9** | API order tests incl. concurrency and server-side pricing; UI checkout | REQ-ORD-01, 02, 03 |
| R4 | Invalid or hostile input causes errors or data damage | 3 | 2 | **6** | Validation and injection cases at API level; manual markup and XSS cases | REQ-SEC-01 |
| R6 | Users with disabilities cannot use the shop | 3 | 2 | **6** | axe-core scans; manual keyboard and screen reader cases | REQ-A11Y-01 |
| R2 | A user reaches another user's data or admin functions | 2 | 3 | **6** | 401 and 403 checks on every protected endpoint; privacy tests | REQ-ADM-01, 02, REQ-WISH-01 |
| R5 | Customers cannot complete a purchase | 2 | 3 | **6** | UI journeys and acceptance scenarios | REQ-CAT-01, 02, REQ-CART-01, REQ-REV-01 |
| R3 | Account takeover through weak sessions or passwords | 1 | 3 | **3** | Hashing, no user enumeration, session lifecycle; manual password policy exploration | REQ-AUTH-01, 02, 03 |
| R7 | UI shows data that differs from the API | 2 | 2 | **4** | UI tests cross-check against the API | REQ-CAT-01, 02 |
| R8 | Slow responses under load | 1 | 2 | **2** | Separate load-test project | REQ-PERF-01 |

## What the first test runs showed

Likelihood was updated with evidence: R1 and R4 were rated 3 because defects D1 and D2 (orders) and D3 to D6 (validation) were found in the first API runs; R6 was rated 3 because the first accessibility scan failed on every customer page. Details in the application repository's `docs/KNOWN_DEFECTS.md`.

## Residual risk

Known gaps with no automated test: no password strength policy, emails are case-sensitive, only Chromium is run, and keyboard and screen reader behaviour has been designed but not yet tested by hand.
