"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

# O(n) Linear Time

# def threes_and_fives(max):
#     sum = 0
#     for i in range(1, max):
#         if i % 3 == 0 or i % 5 == 0:
#             sum += i

#     return sum

# 0(1) Constant Time


def threes_and_fives(maximum, multiple_x, multiple_y):
    return get_multiples(maximum, multiple_x) + get_multiples(999, multiple_y) - get_multiples(999, multiple_x * multiple_y)


def get_multiples(maximum, n):
    multiples = (maximum // n) * (maximum // n + 1) // 2 * n
    return multiples


print(threes_and_fives(1000, 3, 5))
