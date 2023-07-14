# https://leetcode.com/problems/range-sum-query-immutable/

from typing import List


class NumArray:
    # Time O(n)
    def __init__(self, nums: List[int]):
        self.nums = nums

    # Time: O(n) -> but can be improved with prefix sum to O(1)
    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        for i in range(left, right + 1):
            sum += self.nums[i]
        return sum

# TODO: improve by using prefix sum


obj = NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(0, 2))
print(obj.sumRange(2, 5))
print(obj.sumRange(0, 5))
