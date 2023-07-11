# https://leetcode.com/problems/can-place-flowers/

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        for i in range(0, len(flowerbed), 1):
            left = 0
            right = 0
            if i != 0:
                left = flowerbed[i - 1]
            curr = flowerbed[i]
            if i != len(flowerbed) - 1:
                right = flowerbed[i + 1]
            if left == 0 and curr == 0 and right == 0:
                n -= 1
                flowerbed[i] = 1
                if n == 0:
                    return True
        return False


s = Solution()
print(s.canPlaceFlowers([1, 0, 0, 0, 1], 2))  # False
print(s.canPlaceFlowers([1, 0, 0, 0, 1], 1))  # True
print(s.canPlaceFlowers([0, 1], 1))  # False
print(s.canPlaceFlowers([0, 0], 1))  # True
print(s.canPlaceFlowers([1, 0, 1], 0))  # True
