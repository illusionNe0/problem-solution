"""
[383] Ransom Note
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False

        dr, dm = {}, {}
        for i in ransomNote:
            dr[i] = dr.get(i, 0) + 1
        for i in magazine:
            dm[i] = dm.get(i, 0) + 1

        # storing symbols and their frequency in dictionaries

        for k, v in dr.items():
            # check if key (symbol) both in dicts
            # check if number of symbols is enough
            if k not in dm.keys() or v > dm[k]:
                return False
        return True

"""
[205] Isomorphic String
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # guard condition
        if len(s) != len(t):
            return False
        
        sindex = {}
        tindex = {}

        # we fix the indexes with elements
        for i in range(len(s)):
            if s[i] not in sindex:
                sindex[s[i]] = i
            if t[i] not in tindex:
                tindex[t[i]] = i
            if sindex[s[i]] != tindex[t[i]]:
                return False
        return True

"""
[290] Word Pattern
"""
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        ns = s.split()
        
        if len(ns) != len(pattern):
            return False
        # filling dict with related values
        for i in range(len(pattern)):
            if ns[i] in d.values() and pattern[i] not in d.keys():
                return False
            d[pattern[i]] = ns[i]
        # we recreate the original string (list) and compare them if they are equal
        nns = []
        for i in pattern:
            nns += [d[i]]

        return ns == nns

"""
[242] Valid Anagram
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # guard
        if len(s) != len(t):
            return False

        # we will count the number of unique symbols and then just compare two dicts
        d1, d2 = {}, {}
        # for s and t:
        for i in s:
            d1[i] = d1.get(i, 0) + 1
        for j in t:
            d2[j] = d2.get(j, 0) + 1

        return d1 == d2

"""
[49] Group Anagrams
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        d = {}

        # anagrams are equal strings if sorted, then the sorted one can be considered as key
        # and values are uncahnged strings
        for i in strs:
            d.setdefault(''.join(sorted(i)), []).append(i)

        # adding anagrams list in list
        for i in d:
            buffer = []
            for j in d[i]:
                buffer += [j]
            anagrams.append(buffer)
        return anagrams

"""
 [1] Two Sum
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        was = {}
        for i, num in enumerate(nums):
            delta = target - num
            if delta in was:
                return [was[delta], i]
            was[num] = i
        
"""
[202] Happy Number
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        d = {}
        while True:
            res = 0
            # sum of square of digits
            for i in str(n):
                res += int(i)**2
            
            if res == 1:
                return True
            elif res in d.keys() or res in d.values():
                return False
            else:
                d[n] = res
                n = res

"""
[219] Contains Duplicates II
"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dick = {}
        # dick will contain value - index
        # we will iterate in value calculating indexes difference
        for index, value in enumerate(nums):
            dick.setdefault(value, []).append(index)
            for i in dick[value]:
                if abs(i - index) <= k and i != index:
                    return True
        return False

"""
[128] Longest Consecutive Sequence in O(n)
"""

