# https://leetcode.com/problems/powx-n/

class Solution: # O (log n)
    def myPow(self, x: float, n: int) -> float:
        def divideAndConquer(base, n):
            if n == 1:
                return base
            half = divideAndConquer(base, n // 2)
            return half * half if n % 2 == 0 else half * half * base
        if n == 0: return 1
        if x == 0: return 0
        res = divideAndConquer(x, abs(n))
        return res if n > 0 else 1 / res

s = Solution()
print(s.myPow(2.1, 3))
print(s.myPow(2.0, -2))
print(s.myPow(2.0, 10))
