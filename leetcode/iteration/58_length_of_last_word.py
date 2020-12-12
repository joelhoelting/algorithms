"""
Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only.



Example 1:

Input: s = "Hello World"
Output: 5

Example 2:

Input: s = " "
Output: 0

"""


# def lengthOfLastWord(s):
#     # Runtime: 20 ms, faster than 58.47% of Python online submissions for Length of Last Word.
#     # Memory Usage: 14 MB, less than 32.43% of Python online submissions for Length of Last Word.
#     """
#     :type s: str
#     :rtype: int
#     """
#
#     letter_index = 0
#     last_word = 0
#
#     for i in range(0, len(s)):
#         if s[i] == " ":
#             if s[i - 1] != " ":
#                 last_word = letter_index
#                 letter_index = 0
#         else:
#             if i == len(s) - 1:
#                 letter_index += 1
#                 last_word = letter_index
#             else:
#                 letter_index += 1
#
#     print(last_word)
#     return last_word

def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    word_list = s.split(' ')
    new_list = []

    for i in range(0, len(word_list)):
        if word_list[i] != '':
            new_list.append(word_list[i])

    return len(new_list[-1]) if new_list else 0


lengthOfLastWord('happy go lucky')
