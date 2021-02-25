# Write a function that takes a string as input and reverse only the vowels of a string.
#
# Example 1:
#
# Input: "hello"
# Output: "holle"
#
# Example 2:
#
# Input: "leetcode"
# Output: "leotcede"
#
# Note:
# The vowels does not include the letter "y".

def reverseVowels(self, s: str) -> str:
    l = 0
    r = len(s) - 1

    vowels = set(['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'])
    string_to_list = list(s)

    while l < r:
        if set([s[l], s[r]]).issubset(vowels):
            temp = s[l]
            string_to_list[l] = string_to_list[r]
            string_to_list[r] = temp
            l += 1
            # r -= 1
        elif s[l] in vowels:
            r -= 1
        elif s[r] in vowels:
            l += 1
        else:
            l += 1
            r -= 1

    return ''.join(string_to_list)