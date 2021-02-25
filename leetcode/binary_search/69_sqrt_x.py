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

    l = 1
    r = x
    if x < 2:
        return x
    while l < r:
        mid = l + (r - l) // 2

        if mid * mid == x:
            return mid
        if mid * mid > x:
            r = mid
        else:
            l = mid + 1
            
    return l - 1


mySqrt(14)
