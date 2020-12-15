"""
168. Excel Sheet Column Title
Easy

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...

Example 1:

Input: 1
Output: "A"

Example 2:

Input: 28
Output: "AB"

Example 3:

Input: 701
Output: "ZY"
"""


class Solution:
    def convertToTitle(self, n: int) -> str:
        s = ""
        for i in range(65, 91):
            s = s + chr(i)
        st = ""
        while n:
            n = n - 1
            st = s[n % 26] + st
            n = n // 26
        print(st, n)
        return st


Solution().convertToTitle(26)
