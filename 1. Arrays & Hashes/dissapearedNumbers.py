# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

from typing import List

# O(N); S: O(1)


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        missingElements = []
        for i in range(0, len(nums)):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1]
        for j in range(0, len(nums)):
            if nums[j] > 0:
                missingElements.append(j + 1)
        return missingElements


s = Solution()

assert s.findDisappearedNumbers([1, 1]) == [2]
assert s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
