# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

from typing import List


class Solution:
    # O(n) / worst space complexity: O(n)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pairs = {}
        for i, num in enumerate(numbers):
            if num not in pairs:
                pairs[target - num] = i
            else:
                return [pairs[num] + 1, i + 1]

    # O(n) / O(1)
    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                return [i + 1, j + 1]


s = Solution()

assert s.twoSum2([2, 7, 100, 24], 9) == [1, 2]
assert s.twoSum2([-1, 0], -1) == [1, 2]
assert s.twoSum2([2, 3, 4], 6) == [1, 3]
