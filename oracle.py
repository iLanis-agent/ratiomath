#!/usr/bin/env python3
# Ratio Math oracle - mirrors engine.js.
import json, math

def _w(x, label):
    if not math.isfinite(x) or math.floor(x) != x or x < 1 or x > 1000000:
        raise ValueError(label + " must be a whole number from 1 to 1000000")
    return int(x)

def _fmt(h):
    whole, frac = divmod(h, 100)
    if frac == 0:
        return str(whole)
    f = f"{frac:02d}"
    if f[1] == "0":
        f = f[0]
    return f"{whole}.{f}"

def simplest_truth(first, second):
    a = _w(first, "first number"); b = _w(second, "second number")
    g = math.gcd(a, b)
    if g == 1:
        return f"{a}:{b} is already in lowest terms."
    return f"{a}:{b} simplifies to {a // g}:{b // g}."

def split_truth(total, first, second):
    t = _w(total, "total"); a = _w(first, "first part"); b = _w(second, "second part")
    s = a + b
    pa = (t * a) // s; pb = (t * b) // s
    ra = (t * a) % s; rb = (t * b) % s
    left = t - pa - pb
    if left > 0:
        if ra >= rb:
            pa += left
        else:
            pb += left
    head = f"Split {t} as {a}:{b}: {pa} and {pb}"
    if ra == 0 and rb == 0:
        return head + "."
    return head + f", rounded to whole units so they add to {t}."

def fourth_truth(first, second, third):
    a = _w(first, "first number"); b = _w(second, "second number"); c = _w(third, "third number")
    num = b * c
    h = (2 * num * 100 + a) // (2 * a)
    exact = (num * 100) % a == 0
    return f"If {a}:{b} is the same as {c}:x, then x is {'' if exact else 'about '}{_fmt(h)}."

FNS = {"simplestTruth": simplest_truth, "splitTruth": split_truth, "fourthTruth": fourth_truth}

CASES = [
    ("simplestTruth", [12, 18]), ("simplestTruth", [8, 15]), ("simplestTruth", [5, 5]), ("simplestTruth", [1, 1]),
    ("simplestTruth", [1000000, 250000]), ("simplestTruth", [6, 3]), ("simplestTruth", [0, 4]), ("simplestTruth", [4, 0]),
    ("simplestTruth", [2.5, 5]), ("simplestTruth", [5, 1000001]), ("simplestTruth", [-3, 6]),
    ("splitTruth", [100, 3, 2]), ("splitTruth", [10, 1, 2]), ("splitTruth", [10, 1, 1]), ("splitTruth", [1, 1, 1]),
    ("splitTruth", [1, 1, 2]), ("splitTruth", [7, 1, 1]), ("splitTruth", [100, 1, 3]), ("splitTruth", [1000000, 1000000, 1000000]),
    ("splitTruth", [5, 2, 1]), ("splitTruth", [0, 1, 1]), ("splitTruth", [10, 0, 1]), ("splitTruth", [10, 1, 0]),
    ("splitTruth", [1000001, 1, 1]), ("splitTruth", [10.5, 1, 1]),
    ("fourthTruth", [2, 3, 10]), ("fourthTruth", [3, 1, 10]), ("fourthTruth", [4, 1, 6]), ("fourthTruth", [8, 3, 1]),
    ("fourthTruth", [1, 1, 1]), ("fourthTruth", [1000000, 1000000, 1000000]), ("fourthTruth", [3, 2, 1]),
    ("fourthTruth", [0, 1, 1]), ("fourthTruth", [1, 0, 1]), ("fourthTruth", [1, 1, 0]), ("fourthTruth", [1, 1, 1.5]),
    ("fourthTruth", [1, 1000001, 1]),
]

out = []
for fn, args in CASES:
    try:
        exp = FNS[fn](*args)
    except ValueError as e:
        exp = "ERR:" + str(e)
    out.append({"fn": fn, "args": args, "expected": exp})
with open("expected.json", "w") as f:
    json.dump(out, f, indent=1)
    f.write("\n")
print(len(out), "cases")
