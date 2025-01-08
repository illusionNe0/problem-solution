"""
[67] Add Binary
"""
class Solution:
    def toBinary(self, n: int) -> str:
        s = ""
        while n:
            s += str(n % 2)
            n //= 2
        return s[::-1]

    def addBinary(self, a: str, b: str) -> str:
        if a == '0' and b == '0':
            return '0'
        return self.toBinary(int(a, 2) + int(b, 2))

"""
[190] Reverse Bits
"""
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            bit = n & 1           # extract least significant bit 
            res = (res << 1) | bit  # add bit, and move bit in n
            n >>= 1               
        return res
        
"""
[191] Number of 1 Bits
"""
# so i came wth two different solutions
# the first one is bit manipulation, we use bitwise operator to count the number of ones
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count
        
# second solution is to convert number to it's binary representation and count the number of ones
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n)[2:].count('1')
"""

