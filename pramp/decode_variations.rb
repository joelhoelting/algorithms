def decode_variations(s)
  return 0 if s.length.zero? || (s.length == 1 || s[0] == '0')

  helper(s, s.length)
end

def helper(s, n)
  return 1 if n == 0 || n == 1

  count = 0

  puts s, n
  count = helper(s, n - 1) if s[n - 1] > '0'
  count += helper(s, n - 2) if s[n - 2] == '1' || (s[n - 2] == '2' && s[n - 1] < '7')

  count
end

puts decode_variations('27345')
