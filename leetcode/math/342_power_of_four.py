import math

# def isPowerOfFour(n: int) -> bool:
#   if n <= 0:
#     return False

#   while n % 4 == 0:
#     n //= 4
  
#   return n == 1

def isPowerOfFour(n: int) -> bool:
	if n & n-1 == 0 and n % 10 in (1,4,6):
		return True
	return False


print(isPowerOfFour(8))