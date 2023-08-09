# https://leetcode.com/problems/koko-eating-bananas/

from typing import List


class Solution:
    def canEat(self, piles, k, h):
        for pile in piles:
            if pile % k == 0:
                h -= pile // k
            else:
                h -= (pile // k) + 1
            if h < 0:
                return False
        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        minK = r
        while l <= r:
            k = l + ((r - l) // 2)
            if self.canEat(piles, k, h):
                minK = min(k, minK)
                r = k - 1
            else:
                l = k + 1
        return minK


s = Solution()

assert s.minEatingSpeed(piles=[332484035, 524908576, 855865114, 632922376, 222257295, 690155293, 112677673, 679580077, 337406589,
                               290818316, 877337160, 901728858, 679284947, 688210097, 692137887, 718203285, 629455728, 941802184], h=823855818) == 14
assert s.minEatingSpeed(piles=[3, 6, 7, 11], h=8) == 4
assert s.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=6) == 23
assert s.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5) == 30
assert s.minEatingSpeed(piles=[1, 1, 1], h=3) == 1
