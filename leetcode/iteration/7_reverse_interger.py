"""
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.



Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21

Example 4:

Input: x = 0
Output: 0

"""

# def reverse(x):
#     # initial answer -- Passed
#     # Runtime: 24 ms, faster than 44.48% of Python online submissions for Reverse Integer.
#     # Memory Usage: 13.7 MB, less than 13.57% of Python online submissions for Reverse Integer.

#     stringify_x = str(x)
#     negative = False
#     if stringify_x[0] == '-':
#         negative = True
#         stringify_x = stringify_x[1:]

#     new_int_array = [int(i) for i in str(stringify_x)]

#     i = len(new_int_array) - 1
#     while i >= 0:
#         if new_int_array[i] == 0:
#             if len(new_int_array) == 1:
#                 return 0

#             new_int_array.pop()
#             i -= 1
#         else:
#             break

#     final_array = []
#     j = len(new_int_array) - 1
#     while j >= 0:
#         final_array.append(new_int_array[j])
#         j -= 1

#     string_list = [str(integer) for integer in final_array]
#     answer_string = "".join(string_list)
#     integer_conversion = int(answer_string)

#     if -2**31 <= integer_conversion <= 2**31 - 1:
#         return -integer_conversion if negative else integer_conversion
#     else:
#         return 0


# reverse(-123)

# def reverse(x):
#     s = str(x)
#     res = int('-' + s[1:][::-1]) if s[0] == '-' else int(s[::-1])
#     return res if -2147483648 <= res <= 2147483647 else 0


# reverse(6543)


# def reverse(x):
#     res, remains = 0, abs(x)

#     while remains:
#         res, remains = res*10 + remains % 10, remains//10

#     if x < 0:
#         res *= -1

#     return res if abs(res) < 0x7fffffff else 0
