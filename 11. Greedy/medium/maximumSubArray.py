# https://leetcode.com/problems/maximum-subarray/

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]

        prevPrefix = 0
        for n in nums:
            if prevPrefix < 0:
                prevPrefix = 0
            prevPrefix += n
            maxSum = max(maxSum, prevPrefix)
        return maxSum


s = Solution()
assert s.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert s.maxSubArray(nums=[-2, -1, -3]) == -1
