"""

Add Binary

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
