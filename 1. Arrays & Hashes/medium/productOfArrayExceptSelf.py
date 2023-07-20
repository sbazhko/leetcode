# https://leetcode.com/problems/product-of-array-except-self/

from typing import List


class Solution:
    # O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixSum = [1]  # of elems coming before i-th
        suffixSum = [1]  # of elems coming after i-th
        for i in range(1, len(nums)):
            prefixSum.append(prefixSum[i - 1] * nums[i - 1])
        for i in range(len(nums) - 2, -1, -1):
            suffixSum.append(suffixSum[(len(nums) - 2) - i] * nums[i + 1])

        res = []
        for i in range(len(prefixSum)):
            res.append(prefixSum[i] * suffixSum[(len(prefixSum) - 1) - i])
        return res


s = Solution()

assert s.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
# [1, 1, 2, 6]
# [1, 4, 12, 24]
