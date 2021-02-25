function numDecodings(s) {
  if (s.length === 0 || (s.length === 1 && s[0] === '0')) return 0;

  if (s.length === 1) return 1;

  return numDecodingsHelper(s, s.length);
}

function numDecodingsHelper(s = 12311, n = 5) {
  if (n === 0 || n === 1) {
    return 1;
  }

  let count = 0;

  if (s[n - 1] > '0') {
    count = numDecodingsHelper(s, n - 1);
  }

  if (s[n - 2] === '1' || (s[n - 2] === '2' && s[n - 1] < '7')) {
    count += numDecodingsHelper(s, n - 2);
  }

  return count;
}

console.log(numDecodings('12311'));
