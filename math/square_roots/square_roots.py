# Root of Number

# Many times, we need to re-implement basic functions without using any standard library functions already implemented. For example, when designing a chip that requires very little memory space.

# In this question we’ll implement a function root that calculates the n’th root of a number. The function takes a nonnegative number x and a positive integer n, and returns the positive n’th root of x within an error of 0.001 (i.e. suppose the real root is y, then the error is: |y-root(x,n)| and must satisfy |y-root(x,n)| < 0.001).

# O(1) Solution

# u ** n == x
# u == x ** 1/n

# O(log(n)) - Binary Search

def root(x, n):
  l = 0
  r = x
  mid = l + r / 2
  
  while (mid - l >= .001):
    print(l, mid, r)
    if mid ** n == x:
      return mid
    
    if (mid ** n  > x):
      r = mid
    else:
      l = mid
    
    mid = (l + r) / 2
  
  return mid


print(root(7, 3))