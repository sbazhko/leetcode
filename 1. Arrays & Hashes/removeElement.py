# https://leetcode.com/problems/remove-element/

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[idx] = nums[i]
                idx += 1
        return idx


s = Solution()
print(s.removeElement([1, 3, 4, 5, 66, 2, 2, 0, 1], 2))  # 7
print(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))  # 5
print(s.removeElement([3, 2, 2, 3], 3))  # 2
print(s.removeElement([2], 3))  # 1
print(s.removeElement([3], 3))  # 0
print(s.removeElement([3, 3], 3))  # 0
print(s.removeElement([4, 5], 4))  # 1
print(s.removeElement([3, 3], 5))  # 2
print(s.removeElement([3, 2, 2, 3], 3))  # 2
print(s.removeElement([], 3))  # 0
print(s.removeElement([1, 2, 3, 4], 1))  # 3
