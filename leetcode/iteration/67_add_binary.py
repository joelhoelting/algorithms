# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
#
# Input: a = "11", b = "1"
# Output: "100"
#
# Example 2:
#
# Input: a = "1010", b = "1011"
# Output: "10101"


def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    diff = abs(len(a) - len(b))
    if diff != 0:
        if len(a) > len(b):
            b = diff * "0" + b
        else:
            a = diff * "0" + a

    carry = 0
    res = ""

    for i in range(len(a) - 1, -1, -1):
        curr = ""
        if a[i] == "0" and b[i] == "0":
            curr = 0
        elif a[i] == "1" and b[i] == "1":
            curr = 2
        else:
            curr = 1

        if curr + carry == 0:
            res = "0" + res
            carry = 0
        elif curr + carry == 1:
            res = "1" + res
            carry = 0
        elif curr + carry == 2:
            res = "0" + res
            carry = 1
        else:
            res = "1" + res
            carry = 1

    if carry:
        res = "1" + res

    return str(res)


addBinary("1010", "1011")
