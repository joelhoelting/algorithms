"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Example 4:

Input: s = "([)]"
Output: false

Example 5:

Input: s = "{[]}"
Output: true

"""


def isValid(s):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        charMap = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []

        # "[()]"
        for char in s:
            if char in charMap:
                last_value = stack.pop() if stack else "X"
                if last_value != charMap[char]:
                    return False
            else:
                stack.append(char)

        return not stack


isValid("]")
