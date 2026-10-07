# Test plan: E-Commerce web application

Structure follows the ISTQB test plan outline. The application under test is the [Ecom shop](https://github.com/mirzamaazbaig/Ecom) (React client, Express API, PostgreSQL). One tester wrote and ran this plan; there is no team, schedule or budget to describe, so those sections are left out instead of invented.

| | |
|---|---|
| Version | 1.0 |
| Scope of this plan | Functional, security-input, data-integrity and accessibility testing of the web application |
| Related documents | [Requirements](../requirements.yml), [risk register](RISK_REGISTER.md), [traceability matrix](TRACEABILITY.md), [manual test cases](../test-cases/manual-test-cases.csv), [exploratory charters](../exploratory/), the application repository's own test strategy |

## 1. Test items

The React client (Vite), the REST API (`/api/auth`, `/products`, `/orders`, `/reviews`, `/wishlist`) and the PostgreSQL schema, as built from the application's branch under test.

## 2. Features to be tested

All requirements in [`requirements.yml`](../requirements.yml): accounts, catalogue, cart, orders and stock, price integrity, wishlist, reviews, admin functions, input handling and accessibility. Priority follows the risk score in the [risk register](RISK_REGISTER.md): orders and stock first, then access control, then the rest.

## 3. Features not tested

| Not tested | Reason |
|---|---|
| Payments, email, third-party services | The application has none; the receipt feature is a mock |
| Performance under load | Covered by a separate load-test project (REQ-PERF-01) |
| Browsers other than Chromium | Configured but not run; recorded as a gap |
| Real assistive technology | Designed as manual cases MT-001 and MT-002, not yet executed |

## 4. Approach

| Level | How | Where |
|---|---|---|
| API | Automated, with SQL checks of stored rows. Most business rules are tested here. | Playwright (JavaScript) and pytest (Python) |
| UI end-to-end | Automated user journeys with page objects; acceptance scenarios in Gherkin | Playwright, Cucumber |
| Accessibility | Automated axe-core scans (WCAG 2.1 A and AA) | Playwright |
| Exploratory | Time-boxed sessions against written charters | [exploratory/](../exploratory/) |
| Manual | Cases for what automation cannot judge: keyboard use, screen reader, layout, odd input | [manual-test-cases.csv](../test-cases/manual-test-cases.csv) |

Techniques used: equivalence partitioning and boundary values (stock exactly equal, one over; ratings 0, 1, 5, 6), error guessing (SQL fragments, markup in text, double submit), state-based thinking (cart, session, order status), and risk-based prioritisation.

Test design rules: every test creates its own data and can run in parallel; no fixed sleeps; a defect is first a failing test; a new test is proven by running it against the code before the fix.

## 5. Item pass/fail criteria

- A test passes when the observed result equals the expected result in its requirement's acceptance criteria.
- A defect is classed by impact: **High** (money, data, security), **Medium** (wrong behaviour with a workaround), **Low** (cosmetic or unlikely).

## 6. Entry, suspension and exit criteria

| | Criteria |
|---|---|
| Entry | The application starts; the database is created, migrated and seeded |
| Suspension | The application cannot start, or the database is unreachable; testing resumes when the environment is restored |
| Exit for a change | All automated suites pass; no unexplained flaky test; every requirement still has coverage (`tools/traceability.py` passes); no open High defect |

## 7. Test deliverables

Automated test code and CI reports, this plan, the risk register, the traceability matrix, manual cases, charters and session notes, bug reports ([examples](../bug-reports/)), and the defect log in the application repository.

## 8. Environment

Local or CI: Node 22, PostgreSQL 16 started as a GitHub Actions service container, Chromium. Test data is created per test through the API and SQL, never shared.

## 9. Project risks to testing

| Risk | Mitigation |
|---|---|
| The application has no requirements document, so expected behaviour is a judgement | Requirements were written from observed behaviour and flagged as derived; unclear rules (password policy, email case) are recorded as questions, not asserted |
| Manual and exploratory cases are not executed in this repository | They are marked "Designed, not executed"; results are reported only when a session is run |
| Shared test data causes flaky tests | Per-test data; flaky tests are investigated, not retried |

## 10. Open questions for the product owner

1. What is the password policy (length, complexity)?
2. Should emails be case-insensitive (`A@x.com` equals `a@x.com`)?
3. Should the UI offer price sorting high to low?
4. Which browsers and screen sizes must be supported?
