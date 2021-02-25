def decode_variations(digits):
  return helper(digits, len(digits))

def helper(digits, n): 
  count = [0] * (n + 1)
  print(count)

  count[0] = 1 
  count[1] = 1 

  for i in range(2, n + 1): 
    if digits[i - 1] > '0': 
      count[i] = count[i - 1]

    # If second last digit is smaller than 2
    # and last digit is smaller than 7, then
    # last two digits form a valid character 
    if (digits[i - 2] == '1' or (digits[i - 2] == '2' and digits[i - 1] < '7') ): 
      count[i] += count[i - 2]

  return count[n]
 
# Driver Code
digits = "11111"; 
print("Count is" , decode_variations(digits)); 
 