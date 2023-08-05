# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0
        while l <= r:
            m = l + ((r - l) // 2)
            if m ** 2 == x:
                return m
            elif m ** 2 > x:
                r = m - 1
            else:
                l = m + 1
                res = m
        return res


s = Solution()

assert s.mySqrt(4) == 2
assert s.mySqrt(8) == 2
assert s.mySqrt(0) == 0
assert s.mySqrt(1) == 1
assert s.mySqrt(2147395599) == 46339
