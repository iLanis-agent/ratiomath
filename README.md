# Ratio Math

Ratio arithmetic on whole numbers. Split it 3 to 2 and the parts still add up.

## What it computes

- **The simplest-form truth** - divide both sides of a ratio by their greatest common divisor: 12:18 simplifies to 2:3.
- **The split truth** - share a total by a ratio in whole units, with the leftover going to the larger remainder: 100 as 3:2 is 60 and 40.
- **The missing-term truth** - if a:b is the same as c:x, then x is b times c over a, to hundredths: 2:3 is the same as 10:15.

All inputs are whole numbers from 1 to 1000000.

## Boundary

Arithmetic only. Ratio Math does not say what ratio a recipe, mix or deal should use. Check that against its own instructions.

## Files

- `index.html` - landing page.
- `app.html` - the interactive calculator.
- `engine.js` - the arithmetic.
- `oracle.py` - the Python mirror that generates `expected.json`.
- `test.js` - compares every engine output against `expected.json` (37 cases).
- `expected.json` - the golden answers.

## Test

```
python3 oracle.py
node test.js
```

Live: https://ilanis-agent.github.io/ratiomath/
Repo: https://github.com/iLanis-agent/ratiomath
