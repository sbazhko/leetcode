# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    # O (32 len int) -> O(1)
    def hammingWeight(self, n: int) -> int:
        oneCount = 0
        while n:
            oneCount += n % 2  # or n = n & (n - 1); res += 1
            n = n >> 1
        return oneCount
