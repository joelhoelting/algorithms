function root(x, n) {
  // your code goes here
  let l = 0;
  let r = x;
  let mid;

  while (l < r) {
    mid = (r - l) / 2;

    if (Math.pow(mid, n) - x <= 0.001) {
      return mid;
    }

    if (Math.pow(mid, n) > x) {
      r = mid;
    } else {
      l = mid;
    }
  }

  console.log(l);
  return l.toFixed(3);
}

console.log(root(7, 3));

Math.pow(x, 1 / n).toFixed(3);
