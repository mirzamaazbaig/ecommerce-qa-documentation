# D2: The client decides the price it pays

| Field | Value |
|---|---|
| Severity | High |
| Priority | High |
| Area | Orders / API |
| Environment | Application branch under test, Node 22, PostgreSQL 16, Chromium |
| Found by | Automated test written to assert the correct behaviour |
| Status | Fixed and verified |

## Steps to reproduce
1. Choose a product that costs 100.
2. Sign in as a customer.
3. `POST /api/orders` with `items: [{productId, quantity: 1, price: 0.01}]` and `totalAmount: 0.01`.

## Expected result
The order is priced from the catalogue (100); the price and total in the request are ignored.

## Actual result
The order is stored with `price_at_purchase = 0.01` and a total of 0.01.

## Impact
Anyone who can send an HTTP request can buy anything for any price.

## Root cause
`price` and `totalAmount` were read from `req.body` and inserted unchanged.

## Fix
The server reads each price from `products` and computes the total in cents; request prices are ignored.

## Verification
`TC_API_ORDER_012` fails on the old code and passes on the fix. The same tests were run against the code before the fix to prove they fail there.

Source: the application repository's `docs/KNOWN_DEFECTS.md`, entry D2.
