# https://leetcode.com/problems/find-pivot-index/

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sums = [0] * len(nums)
        currSum = 0
        for i in range(len(nums) - 1, -1, -1):
            currSum += nums[i]
            sums[i] += currSum
        currSum = 0
        for i in range(0, len(nums)):
            currSum += nums[i]
            sums[i] -= currSum
            if sums[i] == 0:
                return i
        return -1


s = Solution()

assert s.pivotIndex([1, 7, 3, 6, 5, 6]) == 3
assert s.pivotIndex([1, 2, 3]) == -1
assert s.pivotIndex([2, 1, -1]) == 0
assert s.pivotIndex([-1, -1, 0, 0, -1, -1]) == 2
