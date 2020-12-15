"""
Given an integer n, return the number of trailing zeroes in n!.

Follow up: Could you write a solution that works in logarithmic time complexity?



Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Example 3:

Input: n = 0
Output: 0

"""


# Iterative
class Solution:
    def trailingZeroes(self, n: int) -> int:
        num_of_fives = 0

        while n >= 5:
            n = n // 5
            num_of_fives += n

        return num_of_fives


class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n < 5:  # base case
            return 0
        else:  # add the current factor of 5 to the next smallest factor of n/5
            return int(n / 5) + self.trailingZeroes(int(n / 5))
