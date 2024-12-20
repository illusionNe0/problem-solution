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
