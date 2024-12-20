"""
[9] Palindrome Number
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

"""
[66] Plus One
"""


"""
[172] Factorial Trailing Zeros
"""
from math import factorial

class Solution:
    def trailingZeroes(self, n: int) -> int:
        nfac = factorial(n)

        count = 0
        while nfac % 10 == 0:
            count += 1
            nfac //= 10
        return count
"""
this is my method and it is stupid and bad time complexity, here the another most effective solution:

trailing zeroes will be created because of multiplication of 5 and 2 pairs, we just have to count their number
the final formula for that is n//2^1 + n//2^2 + ... + n//2^k for two and n//5^1 + n//5^2 + ... + n//5^k for five
(it is important to understand that some numbers can have several fives or two in it, for example 100 have two fives: 100 = 4 * 5 * 5

after counting the two and five numbers, we take min from them min(fives, twos), cause only with less number of twos or fives we cna create pairs
BUT in fact, the number of fives will always be less than number of twos thus we can just count the number of fives

class Solution:
    def trailingZeroes(self, n: int) -> int:
        countOfZero = 0
        powerOfFive = 5

        while n//powerOfFive:
            countOfZero+=n//powerOfFive
            powerOfFive*=5
        return powerOfFive
"""

"""
[69] Sqrt(x)
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        
        while l <= r:
            mid = (l + r) // 2
            mids = mid * mid

            if mids == x:
                return mid
            elif mids < x:
                l = mid + 1
            else:
                r = mid - 1
        return r

"""
another solution, i prefer this one:
class Solution:
    def mySqrt(self, x: int) -> int:
        # using newton's sqrt(f(x)) approximation
        # Xn+1 = 1/2 * (Xn + a/Xn)

        # in this problem i chose X0 as a/2
        # and the number of iterations as 20 (it was enough)
        if x == 0:
            return 0

        xn = x / 2
        for i in range(20):
            xn = 0.5 * (xn + x/xn)
        return int(xn)
"""



