# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minEl = 5001
        while l <= r:
            m = l + ((r - l) // 2)
            if nums[l] < nums[r]:
                minEl = min(minEl, nums[l])

            minEl = min(minEl, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return minEl


s = Solution()

assert s.findMin(nums=[1]) == 1
assert s.findMin(nums=[1, 2]) == 1
assert s.findMin(nums=[3, 1, 2]) == 1
assert s.findMin(nums=[3, 4, 5, 1, 2]) == 1
assert s.findMin(nums=[5, 6, 7, 0, 1, 2, 3, 4]) == 0
assert s.findMin(nums=[6, 7, 0, 1, 2, 3, 4, 5]) == 0
assert s.findMin(nums=[11, 13, 15, 17]) == 11
assert s.findMin(nums=[2, 3, 4, 5, 1]) == 1
