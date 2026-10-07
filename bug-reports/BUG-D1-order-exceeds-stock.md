# D1: Order for more than the available stock is accepted and stock goes negative

| Field | Value |
|---|---|
| Severity | High |
| Priority | High |
| Area | Orders / API |
| Environment | Application branch under test, Node 22, PostgreSQL 16, Chromium |
| Found by | Automated test written to assert the correct behaviour |
| Status | Fixed and verified |

## Steps to reproduce
1. Create a product with stock 2 (admin, `POST /api/products`).
2. Sign in as a customer.
3. `POST /api/orders` with that product and `quantity: 5`.

## Expected result
`409` with an insufficient-stock message; no order is created; stock stays 2.

## Actual result
`201 Created`; the order is stored and stock becomes -3 (the table has no `CHECK (stock >= 0)`).

## Impact
The shop sells goods it does not have. Customers are charged for orders it cannot fulfil, and the negative stock hides the problem.

## Root cause
`UPDATE products SET stock = stock - $1` ran without checking the current stock.

## Fix
Product rows are locked (`SELECT ... FOR UPDATE`) inside the order transaction; every line is checked before anything is written; an unavailable line rejects the whole order with 409.

## Verification
`TC_API_ORDER_009`, `010`, `011`, `015`, `016` fail on the old code and pass on the fix. The same tests were run against the code before the fix to prove they fail there.

Source: the application repository's `docs/KNOWN_DEFECTS.md`, entry D1.
