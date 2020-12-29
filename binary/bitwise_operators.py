# ----------------------------------------
# "bitwise right shift" ('>>' Operator)
# Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). 
# This is the same as multiplying x by 2**y. 

a = 240  # 11110000
a >> 2  # 00111100 -> 60

a = 79  # 1001111
a >> 2  # 0010011 -> 19

# ----------------------------------------
# "bitwise right left" ('<<' Operator)
# Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y.
a = 66  # 1000010
a >> 2  # 001010000 -> 80

a = 99  # 1100011
a >> 3  # 0001100 -> 12

# ----------------------------------------
# "bitwise and" ('&' Operator)
# Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.
a = 40  # 101000
b = 23  # 010111
print(a & b)  # 000000 --> 0

a = 124  # 1111100
b = 125  # 1111101
print(a & b)  # 1111100 --> 124

# "bitwise or" ('|'operator)
# Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1. 
a = 55  # 110111
b = 28  # 011100
print(a | b)  # 111111 --> 63

a = 49  # 110001
b = 19  # 010011
print(a | b)  # 110011 --> 51

# "bitwise INVERSION" ('~'operator)
# ~ x
# Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. 
# This is the same as -x - 1.

a = 65  # 1000001
~a  # 0111110 -> 62

a = 0b1111  # 15
b = 0b1100  # 12
a - b == 3

65 + ~65 == -1

# "bitwise EXCLUSIVE OR / XOR" ('^' operator)
# x ^ y Does a "bitwise exclusive or".
# Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, 
# and it's the complement of the bit in x if that bit in y is 1. 

bin(0b1111 ^ 0b1111)
# '0b0'
bin(0b1111 ^ 0b0000)
# '0b1111'
bin(0b0000 ^ 0b1111)
# '0b1111'
bin(0b1010 ^ 0b1111)
# '0b101'

# this example swaps integers without a temporary variable using XOR
a = 2
b = 8
a ^= b
b ^= a
a ^= b
a  # => 8
b  # => 2
