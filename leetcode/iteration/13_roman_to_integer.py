"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.
"""


def roman_to_integer(s):
    symbol_hash = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000
    }

    exception_array = ["IV", "IX", "XL", "XC", "CD", "CM"]

    max_index = len(s) - 1
    counter = 0
    sum = 0

    while counter <= max_index:
        print(counter)
        if counter < max_index and s[counter] + s[counter + 1] in exception_array:
            exception = s[counter] + s[counter + 1]
            sum += symbol_hash[exception]
            counter += 2
        else:
            sum += symbol_hash[s[counter]]
            counter += 1

    print(sum)
    return sum


# def roman_to_integer(s):
#     mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#     num, temp = 0, 0
#     for i, c in enumerate(s[0:-1]):
#         if mapping[c] < mapping[s[i+1]]:
#             temp = mapping[c]
#         else:
#             num += (mapping[c] - temp)
#             temp = 0

#     return num + (mapping[s[-1]] - temp)

# def roman_to_integer(s):
#     r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

#     sum = 0
#     for i in range(len(s)-1):
#         print(i)
#         if r[s[i]] < r[s[i+1]]:
#             sum -= r[s[i]]
#         else:
#             sum += r[s[i]]

#     sum += r[s[-1]]
#     return sum


roman_to_integer("CDV")
