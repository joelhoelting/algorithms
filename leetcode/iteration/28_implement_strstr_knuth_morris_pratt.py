"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
"""


def kmp(string="pieapple", substring="app"):
    """return all matching positions of p in t"""
    next = [0]
    j = 0

    # j = 0
    # i = 2
    # next = [0, 0, 0]
    for i in range(1, len(substring)):
        while j > 0 and substring[j] != substring[i]:
            j = next[j - 1]
        if substring[j] == substring[i]:
            j += 1
        next.append(j)

    print(next)

    # the search part and build part is almost identical.
    ans = []
    j = 0

    for i in range(len(string)):
        while j > 0 and string[i] != substring[j]:
            j = next[j - 1]
        if string[i] == substring[j]:
            j += 1
        if j == len(substring):
            ans.append(i - (j - 1))
            j = next[j - 1]

    return ans


def test():
    kmp('pieapple', 'app')
    # p1 = "aa"
    # t1 = "aaaaaaaa"

    # assert(kmp(t1, p1) == [0, 1, 2, 3, 4, 5, 6])

    # p2 = "abc"
    # t2 = "abdabeabfabc"

    # assert(kmp(t2, p2) == [9])

    # p3 = "aab"
    # t3 = "aaabaacbaab"

    # assert(kmp(t3, p3) == [1, 8])

    # print("all test pass")


if __name__ == "__main__":
    test()
