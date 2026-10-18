// Ratio Math engine - simplify a ratio, split a total by a ratio, find the missing fourth term.
// Mirrored by oracle.py; keep the op order identical.
// All inputs are whole numbers. The missing term comes out to hundredths.

function _w(x, label) {
  if (!isFinite(x) || Math.floor(x) !== x || x < 1 || x > 1000000) {
    throw new Error(label + " must be a whole number from 1 to 1000000");
  }
  return x;
}

function _gcd(a, b) {
  while (b !== 0) { var t = a % b; a = b; b = t; }
  return a;
}

function _fmt(h) {
  var whole = Math.floor(h / 100), frac = h % 100;
  if (frac === 0) return String(whole);
  var f = (frac < 10 ? "0" : "") + frac;
  if (f.charAt(1) === "0") f = f.charAt(0);
  return whole + "." + f;
}

// The simplest-form truth: divide both sides by their greatest common divisor.
function simplestTruth(first, second) {
  var a = _w(first, "first number"), b = _w(second, "second number");
  var g = _gcd(a, b);
  if (g === 1) return a + ":" + b + " is already in lowest terms.";
  return a + ":" + b + " simplifies to " + (a / g) + ":" + (b / g) + ".";
}

// The split truth: share a total by a ratio, whole units, parts add back to the total.
function splitTruth(total, first, second) {
  var t = _w(total, "total"), a = _w(first, "first part"), b = _w(second, "second part");
  var s = a + b;
  var pa = Math.floor(t * a / s), pb = Math.floor(t * b / s);
  var ra = (t * a) % s, rb = (t * b) % s;
  var left = t - pa - pb;
  if (left > 0) {
    if (ra >= rb) pa += left; else pb += left;
  }
  var head = "Split " + t + " as " + a + ":" + b + ": " + pa + " and " + pb;
  if (ra === 0 && rb === 0) return head + ".";
  return head + ", rounded to whole units so they add to " + t + ".";
}

// The fourth truth: a:b is the same as c:x, so x is b times c over a.
function fourthTruth(first, second, third) {
  var a = _w(first, "first number"), b = _w(second, "second number"), c = _w(third, "third number");
  var num = b * c;
  var h = Math.floor((2 * num * 100 + a) / (2 * a));
  var exact = (num * 100) % a === 0;
  return "If " + a + ":" + b + " is the same as " + c + ":x, then x is " + (exact ? "" : "about ") + _fmt(h) + ".";
}
