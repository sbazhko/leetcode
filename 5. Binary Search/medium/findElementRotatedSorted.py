# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if target == nums[m]:
                return m
            # we are on the right
            if nums[m] < nums[l]:
                if target > nums[r] or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # we're on the left
            else:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
        return -1


s = Solution()

assert s.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0) == 4
assert s.search(nums=[4, 5, 6, 7, 0, 1, 2], target=3) == -1
assert s.search(nums=[1], target=3) == -1
