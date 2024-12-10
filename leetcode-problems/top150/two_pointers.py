"""
so i decided to divide topics in leetocde 150 poblems by files, i think its better

* but the numeration continues
"""

# (25) [125] valid palindrome
class Solution:
    def isPalindrome(sels, s: str) -> bool:
        ns = s.strip().lower()
        # i fucking tired to try to solve with two pointers, i used magic of python aahahah
        # and this turn out to be one of the most effective way
        # this is the easiest way i guess, anyway i'll put two pointer method of solution in the comments
        l = ''
        for i in ns:
            if i.isalnum(): l += i
        return l[:] == l[::-1]
"""
two pointer solution: 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0           # left
        r = len(s) - 1  # right
        
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
                
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
            
        return True
"""

# (26) [392] is subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True
        elif len(t) == 0: return False
        # well well well
        k = 0 # pointer to s
        # k has to be equal to length of the s
        for i in range(len(t)):
            if t[i] == s[k]:
                k += 1
            if k == len(s):
                return True
        return False
        

# (27) [167] two sum II - input array sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # we have to use fact that array is sorted
        # we can subtract element of array from target and then using search find a number in array so that their sum would give target value
        for i in range(len(numbers)):
            delta = target - numbers[i]

            try:
                k = numbers.index(delta)
            except ValueError:
                k = -1

            if k != -1 and i != k:
                if i < k: return [i + 1, k + 1]
                else: return [k + 1, i + 1]
        return []

    # wtffff i forgot that .index() method returns exception error if there is no index found
    # first i thought to write binary search but instead just use try catch (try except)
"""
it turned out that solution is extremely slow, so i put here more effective one
also this solution uses two pointers sooo it is even better i guess
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0 # left
        j = len(numbers) - 1 # right
        while i < j:
            if numbers[i] + numbers[j] == target:
                if i < j:
                    return [i + 1, j + 1]
                else:
                    return [j + 1, i + 1]
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1
        return []
"""

# (28) [11] container with most water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0 # left
        j = len(height) - 1 # right
        area = -1

        while i < j:
            temp = min(height[i], height[j]) * (j - i) # formula to find area
            if temp > area:
                area = temp
            
            # keep greater height
            if height[i] > height[j]: j -= 1
            else: i += 1
        
        return area

# (29) [15] 3sum
