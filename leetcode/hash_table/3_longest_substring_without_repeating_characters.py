# def lengthOfLongestSubstring(self, s: str) -> int:
#     global_max = 0
#     temp_max = 0
#
#     char_map = dict()
#
#     # char_map = { a: 0, l: 1, p: 2, h: 3 }
#     # temp_max = 1, 2, 3, 4,
#     # global_max = 0, 0, 0, 0, 4
#
#     i = 0
#     while i < len(s):
#         if s[i] in char_map:
#             if temp_max > global_max:
#                 global_max = temp_max
#
#             temp_next_index = char_map[s[i]] + 1
#             i = temp_next_index
#             char_map = {}
#             temp_max = 0
#
#         else:
#             char_map[s[i]] = i
#             i += 1
#             temp_max += 1
#
#     if temp_max > global_max:
#         global_max = temp_max
#
#     return global_max

def lengthOfLongestSubstring(self, s: str) -> int:
    char_set = set()
    l = r = max_length = 0

    while r < len(s):
        if s[r] not in char_set:
            char_set.add(s[r])
            max_length = max(max_length, len(char_set))
            r += 1

        else:
            char_set.remove(s[l])
            l += 1

    return max_length

