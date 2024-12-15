# () [9] Palindrome Number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

# () [66] Plus One

# () [172] Factorial Trailing Zeros

# () [69] Sqrt(x)
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
another solution, i prefer this one
"""



