# Recursion and Divide & Conquer

# Runtime: 
# Best Case: O(n log n)
# Worst Case: O(n^2)

from typing import List

def sort(array: List[int] = [9,7,5,11,12,2,14,3,10,6]) -> List[int]:
  less = []
  equal = []
  greater = []

  if len(array) > 1:
    pivot = array[len(array) - 1]
    for x in array:
      if x < pivot:
        less.append(x)
      elif x == pivot:
        equal.append(x)
      elif x > pivot:
        greater.append(x)
    return sort(less)+equal+sort(greater)
  else:  
    # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
    return array

print(sort([5,3,2,8,5,3,12]))