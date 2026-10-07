# E-Commerce QA Documentation: Test Plan, Requirements, Traceability

[![Traceability](https://github.com/mirzamaazbaig/ecommerce-qa-documentation/actions/workflows/traceability.yml/badge.svg)](https://github.com/mirzamaazbaig/ecommerce-qa-documentation/actions/workflows/traceability.yml)

The planning and analysis side of testing the [Ecom shop](https://github.com/mirzamaazbaig/Ecom): requirements with acceptance criteria, a risk-based test plan, manual and exploratory test design, bug reports, and a traceability matrix that is generated and checked by code against the real automated test suites.

The automation lives in other repositories; this one shows how the testing was planned and how the pieces are tied together.

## Contents

| Path | What it is |
|---|---|
| [`requirements.yml`](requirements.yml) | 17 requirements as user stories with acceptance criteria, linked to risks and tests |
| [`docs/TEST_PLAN.md`](docs/TEST_PLAN.md) | Test plan (ISTQB outline): scope, approach, criteria, risks, open questions |
| [`docs/RISK_REGISTER.md`](docs/RISK_REGISTER.md) | Scored product risks and the tests that address each |
| [`docs/TRACEABILITY.md`](docs/TRACEABILITY.md) | Requirement to test matrix, **generated** |
| [`test-cases/manual-test-cases.csv`](test-cases/manual-test-cases.csv) | 14 manual and exploratory cases (CSV, importable into a test management tool) |
| [`exploratory/CHARTERS.md`](exploratory/CHARTERS.md) | Four session charters and a notes template |
| [`bug-reports/`](bug-reports/) | Five real defects written up as tracker-style reports |
| [`tools/traceability.py`](tools/traceability.py) | Builds the matrix and fails the build if it is not trustworthy |

## The traceability check

```bash
pip install -r requirements.txt
python tools/traceability.py --app-repo path/to/Ecom     # writes docs/TRACEABILITY.md
pytest                                                   # tests of the tool itself
```

It fails (exit code 1) when:
- a requirement names an automated test that no longer exists in the application repository;
- a requirement names a manual case that is missing, or that belongs to another requirement;
- a requirement has no coverage and no note saying where it is covered.

The matrix also lists automated tests that no requirement points to. Today all 140 are linked.

## Honest status

- The requirements were **derived from the application as built**, because it has no requirements document. Unclear rules are listed as open questions in the test plan, not asserted.
- The 14 manual cases and 4 charters are **designed, not executed**. Their status column says so. No results are claimed.
- The five bug reports are the real defects from the application's defect log, all fixed and verified by automated tests that fail on the old code.

## Checks done

- The traceability tool has 10 unit tests; disabling its "unknown test id" check makes two of them fail.
- Run against the application repository, it finds 140 automated tests, links all of them, and reports no problems.
