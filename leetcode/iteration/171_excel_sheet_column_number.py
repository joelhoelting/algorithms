"""
https://leetcode.com/problems/excel-sheet-column-number/discuss/818469/Python%3A-the-only-explanation-that-is-understandable-and-makes-sense-to-those-who-just-start

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...

Example 1:

Input: "A"
Output: 1

Example 2:

Input: "AB"
Output: 28

Example 3:

Input: "ZY"
Output: 701

"""


class Solution:
    def titleToNumber(self, s: str) -> int:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper()
        alph_arr = [letter for letter in alphabet]
        num_arr = [i for i in range(1, len(alph_arr) + 1)]
        d = dict(zip(alph_arr, num_arr))

        total = 0
        for letter in s:
            total = total * 26 + d[letter]

        return total
