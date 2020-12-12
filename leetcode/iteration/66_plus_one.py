"""
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

Example 3:

Input: digits = [0]
Output: [1]

"""


def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    if digits[-1] < 9:
        digits[-1] += 1
        return digits

    carry = 1
    for i in range(len(digits) - 1, -1, -1):
        digits[i] += carry
        if digits[i] == 10:
            carry = 1
            digits[i] = 0
        else:
            carry = 0
            break

    if carry:
        digits.insert(0, carry)

    return digits


# def plusOne(digits):
#     """
#     :type digits: List[int]
#     :rtype: List[int]
#     """
#
#     if digits[-1] < 9:
#         digits[-1] += 1
#
#     else:
#         digits = [str(x) for x in digits]
#
#         num = list(str(int("".join(digits)) + 1))
#         return num


plusOne([9, 0, 0, 1])
