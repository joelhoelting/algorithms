# O(log(n)) Time Complexity
def isPowerOfThree(self, n: int) -> bool:
#         if n == 0:
#             return False
        
#         while n % 3 == 0:
#             n //= 3
#         return n == 1

# O(n) Time Complexity
def isPowerOfThree(self, n: int) -> bool:
  max_int = 2 ** 31 - 1
  max_power_three = pow(3, math.log(max_int) // math.log(3))
  return n > 0 and max_power_three % n == 0