"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
"""


def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if not needle:
        print(0)
        return 0

    haystack_len = len(haystack)
    needle_len = len(needle)

    needle_max_length = len(needle)

    i = 0
    while i <= haystack_len - needle_len:
        index = 0
        for j in range(0, needle_len):
            if haystack[i + index] == needle[j]:
                index += 1
            else:
                break

            if index == needle_max_length:
                print(i)
                return i

        i += 1

    print(-1)
    return -1


strStr('funnyman', 'man')
