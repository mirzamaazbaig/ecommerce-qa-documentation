# Exploratory testing charters

Session-based test management: each charter has a mission, a time box and the questions to answer. **None of these sessions has been run yet**, so there are no findings below. When one is run, add a dated notes file next to this one using the template at the end, with real observations, bugs and questions.

| Charter | Mission | Time box | Related risk |
|---|---|---|---|
| EX-01 Checkout under stress | Explore the cart and checkout with unusual sequences (double click, Back button, two tabs, expiring session, stock changing while the cart is open) to find ways to get a wrong or duplicate order | 60 min | R1 |
| EX-02 Hostile text | Explore every place where text is entered or shown (search, review comment, product name, email) with markup, scripts, very long text, emoji and right-to-left text to find places that break or execute it | 45 min | R4 |
| EX-03 Keyboard and screen reader | Explore the main journeys without a mouse, then with a screen reader, to find anything unreachable, unlabeled or unannounced that automated scans cannot judge | 60 min | R6 |
| EX-04 Small screens | Explore the shop at 375 px and 768 px width, in both orientations, to find overlapping, cut-off or untappable content | 30 min | R5 |

## Notes template

```
Charter:        EX-xx
Date / tester:
Build tested:
Time spent:     (setup / testing / bug investigation)
Areas covered:
Bugs found:     (id, one line each, link to report)
Questions:      (things the requirements do not answer)
Ideas for next session:
Coverage vs charter: (what was not looked at)
```
