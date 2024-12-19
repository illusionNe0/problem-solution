# [35] Search Insert Position
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return l


# [74] Ssearch a 2D Matrix
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # FUCKING O(LOG(M*N)) COMPLEXITY..

        l, r = 0, len(matrix) - 1

        # we'll use binary search for matrix[m] where target 'can be' in
        while l <= r:
            m = (l + r) // 2
            if matrix[m][0] <= target <= matrix[m][-1]:
                if matrix[m].count(target) != 0:
                    return True
                else:
                    return False
            elif matrix[m][0] > target:
                r = m - 1
            else:
                l = m + 1
        return False

