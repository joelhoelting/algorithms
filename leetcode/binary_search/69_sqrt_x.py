# Given a non-negative integer x, compute and return the square root of x.
# Since the return type is an integer, the decimal digits are truncated, and only the
# integer part of the result is returned.

# def mySqrt(x):
#     """
#     :type x: int
#     :rtype: int
#     Runtime: 4564 ms, faster than 5.05% of Python online submissions for Sqrt(x).
#     Memory Usage: 13.4 MB, less than 30.61% of Python online submissions for Sqrt(x).
#     """
#
#     if x == 0:
#         return 0
#
#     for i in range(1, x + 1):
#         lower_product = i * i
#         upper_product = (i + 1) * (i + 1)
#
#         if lower_product == x or lower_product < x < upper_product:
#             print(i)
#             return i

def mySqrt(x):
    """
    :type x: int
    :rtype: int
    Runtime: 4564 ms, faster than 5.05% of Python online submissions for Sqrt(x).
    Memory Usage: 13.4 MB, less than 30.61% of Python online submissions for Sqrt(x).
    """

    if x < 2:
        return x

    left_pointer = 1
    right_pointer = x

    while left_pointer < right_pointer:
        mid = left_pointer + right_pointer // 2

        print(left_pointer, right_pointer)
        if mid * mid == x:
            return mid
        elif mid * mid > x:
            right_pointer = mid
        elif mid * mid < x:
            left_pointer = mid + 1

    return left_pointer - 1


mySqrt(14)
