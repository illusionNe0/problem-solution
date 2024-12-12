"""
TOP 150 INTERVIEW QUESTIONS FROM LEETCODE
LET'S GO? (SOSAL?)
"""

"""
here will be my notes or news idk 

4.12.2024 - i will use python3, because it is new and new things are cool, right? (sosal?)
"""

# (1) [88] merge sorted arrays
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        for i in range(m, m + n): # starting change tale elements of nums1 with nums2 elements
            nums1[i] = nums2[j]
            j += 1
        nums1.sort() # sort final array

# (2) [27] remove elemente
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0 # fixing a starter pointer
        for j in range(len(nums)):
            if nums[j] != val:
                # if element differs from value then add to the head of the array
                nums[i] = nums[j]
                i += 1
        return i

# (3) [26] remove duplicates from sorted array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: # if array is empty bam return 0 immediatetly
            return 0
        k = 1 # first element is fixed always
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]: # not duplicate element we move to the head of the array
                nums[k] = nums[i]
                k += 1
        return k

# (4) [80] remove duplicates from sorted array

# (5) [169] majority element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        was = [] # this is like a dictionary
        for i in nums: # if there is same element we just skip iterations
            if i not in was: # if not, then we count it and compare with length // 2
                n = nums.count(i)
                if n > len(nums) // 2:
                    return i
                was += [i]

# (6) [189] rotate array

# (7) [121] best time to buy and sell stock
min_price = 100000000000 # set min price
        max_profit = 0 # set max profit 
        for i in range(len(prices)): # we will find min price every time and at the same time potential max profit
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit

# (8) [122] best time to buy and sell stock II
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sum: int = 0 # init sum
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]: # just calculate if it is positive profit or not
                sum += prices[i] - prices[i - 1]

        return sum

# (9) [55] jump game
# (10) [45] jump game II
# (11) [274] h index
# (12) [380] insert, delete, get random O(1)
# (13) [238] product of array itself
# (14) [134] gas station
# (15) [135] candy
# (16) [42] trapping rain water

# (17) [13] roman to integer
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        res = 0
        # IV, IX, XL, XC, CD, CM
        for i in range(len(s)):
            # checking special cases like 4, 9, ...
            # the logic is that, for example IV it is simply just -1 + 5, here I before V is -1 and V is just V which is 5
            if s[i] == "I" and i < len(s) - 1 and (s[i + 1] == "V" or s[i + 1] == "X"):
                res += -1
            elif s[i] == "X" and i < len(s) - 1 and (s[i + 1] == "L" or s[i + 1] == "C"):
                res += -10
            elif s[i] == "C" and i < len(s) - 1 and (s[i + 1] == "D" or s[i + 1] == "M"):
                res += -100
            else:
                res += d[s[i]]
        return res


# (18) [12] integer to roman
class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1] # nums list
        roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"] # roman list
        s = ''
        for i in range(len(values)):
            # basically each element in values represents respect roman symbol
            # so we use this opportunity
            while num >= values[i]:
                num -= values[i]
                s += roman[i]
        
        return s

# (19) [58] length of last word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # easy ahhaha
        ns = s.strip().split()
        return len(ns[-1])

# (20) [14] longest common prefix


# (21) [151] reverse words in strings
class Solution:
    def reverseWords(self, s: str) -> str:
        # using python magic! just use methods
        ns = s.split()
        ns.reverse()
        return ' '.join(ns)
        # ezzz 0ms runtime

# (22) [6] zigzag conversion
# (23) [28] find the index of first occurence in a string
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # again, not even a problem
        # single line of code...
        return haystack.find(needle)

# (24) [68] text justification
