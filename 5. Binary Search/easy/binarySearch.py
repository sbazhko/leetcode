# https://leetcode.com/problems/binary-search/description/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        mid = r
        while l <= r:
            mid = (l + r) // 2
            if target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                return mid
        return -1


s = Solution()

assert s.search([-1, 0, 3, 5, 9, 12], 9) == 4
assert s.search([-1, 0, 3, 5, 9, 12], 2) == -1
assert s.search([5], 5) == 0
