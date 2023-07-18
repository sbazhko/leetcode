# https://leetcode.com/problems/two-sum/
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        leftToSumUp = {}
        for idx, num in enumerate(nums):
            if num in leftToSumUp:
                return [idx, leftToSumUp[num]]
            leftToSumUp[target - num] = idx
        return []


solution = Solution()
print(solution.twoSum([2,7,11,15], 26))
print(solution.twoSum([3, 2, -1, -2], 0))