# memoization

# def fibonacci_number(n):
#   if n <= 1:
#     return n

#   return memoize(n)  

# def memoize(n):
#   memo = { 0: 0, 1: 1}

#   for i in range(2, n + 1):
#     memo[i] = memo[i-2] + memo[i-1]
  
#   return memo[i]

# recursion

# def fibonacci_number(n):
#   if n <= 1:
#     return n

#   return fibonacci_number(n - 2) + fibonacci_number(n - 1)

# binet's formula
def fibonacci_number(n):
  gr = (1 + 5 ** .5) / 2
  return int((gr ** n + 1) / 5 ** .5)

print(fibonacci_number(1002))
