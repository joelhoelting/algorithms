"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""


# def longestCommonPrefix(strs):
#     Runtime: 16 ms, faster than 94.49% of Python online submissions for Longest Common Prefix.
#     Memory Usage: 13.6 MB, less than 56.08% of Python online submissions for Longest Common Prefix.
#     """
#     :type strs: List[str]
#     :rtype: str
#     """
#     if len(strs) == 0:
#         return ""

#     smallest_word_length = len(strs[0])

#     for word in strs:
#         if len(word) < smallest_word_length:
#             smallest_word_length = len(word)

#     max_index = smallest_word_length - 1

#     prefix_str = ""
#     index_counter = 0

#     while index_counter <= max_index:
#         letter_to_compare = strs[0][index_counter]

#         for word in strs:
#             if word[index_counter] != letter_to_compare:
#                 return prefix_str

#         prefix_str += letter_to_compare
#         index_counter += 1

#     return prefix_str

def longestCommonPrefix(strs):
    prefix = ""

    if strs == []:
        return ""

    for letter_index in range(0, len(strs[0])):
        current_letter = strs[0][letter_index]

        for index in range(1, len(strs)):
            if letter_index > len(strs[index]) - 1:
                return prefix
            if not current_letter == strs[index][letter_index]:
                return prefix
        prefix += current_letter
    return prefix


longestCommonPrefix(["cameloen", "careen", "caravan"])
