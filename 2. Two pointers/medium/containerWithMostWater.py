# https://leetcode.com/problems/container-with-most-water/

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        maxArea = 0
        while i < j:
            side = min(height[i], height[j])
            maxArea = max(side * (j - i), maxArea)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxArea


s = Solution()

assert s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert s.maxArea([1, 1]) == 1
