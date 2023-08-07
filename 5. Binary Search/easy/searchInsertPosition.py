# https://leetcode.com/problems/search-insert-position/

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            if target == nums[m]:
                return m
            if target > nums[m]:
                l = m + 1
            if target < nums[m]:
                r = m - 1
        return l


s = Solution()

assert s.searchInsert(nums=[1, 3, 5, 6], target=5) == 2
assert s.searchInsert(nums=[1, 3, 5, 6], target=7) == 4
assert s.searchInsert(nums=[1, 3, 5, 6], target=2) == 1
