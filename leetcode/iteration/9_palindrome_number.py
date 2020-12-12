"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Follow up: Could you solve it without converting the integer to a string?
"""


# def isPalindrome(x):
# Runtime: 164 ms, faster than 5.19% of Python online submissions for Palindrome Number.
# Memory Usage: 13.7 MB, less than 13.11% of Python online submissions for Palindrome Number.
#     """
#     :type x: int
#     :rtype: bool
#     """

#     if x < 0:
#         return False

#     num_of_places = 0
#     temp_x = x

#     while temp_x != 0:
#         temp_x = temp_x // 10
#         num_of_places += 1

#     left_pointer = num_of_places - 1
#     right_pointer = 0

#     def get_digit(number, idx):
#         return number // 10 ** idx % 10

#     while left_pointer > right_pointer:
#         left_pointer_num = get_digit(x, left_pointer)
#         right_pointer_num = get_digit(x, right_pointer)

#         print(left_pointer_num, right_pointer_num)
#         if left_pointer_num != right_pointer_num:
#             print(False)
#             return False

#         left_pointer -= 1
#         right_pointer += 1

#     print(True)
#     return True


# isPalindrome(122222343222221)

# ex. 49
# reversed        original
# 0               49

# 49 % 10 = 9
# 0 x 10 == 0
# 9+0 = 9
# 49//10 = 4

# 9               4

# 4 % 10 = 4
# 9 x 10 = 90
# 4 + 90 = 94
# 4//10 = 0

# 94              0

def isPalindrome(x):
    if x < 0:
        return False

    current = x
    reversed = 0

    while current != 0:
        reversed = (current % 10) + (reversed * 10)
        current = current // 10
        print(reversed, current)

    print(x == reversed)
    return x == reversed


isPalindrome(4224)
