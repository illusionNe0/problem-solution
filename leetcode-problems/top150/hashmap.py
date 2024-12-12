# (number) Ransom Note [383]
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
