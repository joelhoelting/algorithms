# Reverse bits of a given 32 bits unsigned integer.

# Note:

#     Note that in some languages such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
#     In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.

# Follow up:

# If this function is called many times, how would you optimize it?

 
# Example 1:

# Input: n = 00000010100101000001111010011100
# Output:    964176192 (00111001011110000010100101000000)
# Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

# Example 2:

# Input: n = 11111111111111111111111111111101
# Output:   3221225471 (10111111111111111111111111111111)
# Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.

# A) Bit Manipulation

# In this algorithm, we basically print each bit into its reversed counterpart.

class Solution:
    def reverseBits(self, n):
        res    = 0
        for i in range(32):
            if n&1:
                res += 1 << (31-i)
            n >>= 1
        return res

# B) String Padding
# We can take advantage of the Python's 'bin' function to obtain a string representation of the binary number, add padding zeros, and convert the reversed string back into a number:

class Solution:
    def reverseBits(self, n):
        n = bin(n)[2:]         # convert to binary, and remove the usual 0b prefix
        n = '%32s' % n         # print number into a pre-formatted string with space-padding
        n = n.replace(' ','0') # Convert the useful space-padding into zeros
        # Now we have a  proper binary representation, so we can make the final transformation
        return int(n[::-1],2)

# C) One-Liner String Padding Conversion
# Solution B in One-Liner format.

class Solution:
    def reverseBits(self, n):
        return int( ('%32s' % bin(n)[2:]).replace(' ','0')[::-1] ,2)


# D) High-Speed Code
# I ran a benchmark in my laptop with 1 million random test cases, and this Solution proved to be faster than all previous versions:

class Solution:
    def reverseBits(self, n):
        n = bin(n)[2:]
        n = '0'*( 32-len(n) ) + n
        return int( n[::-1] ,2)
