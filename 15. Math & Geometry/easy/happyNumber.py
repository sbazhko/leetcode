# https://leetcode.com/problems/happy-number/

class Solution:  # O(n)
    def sumOfSquares(self, n: int) -> int:
        out = 0
        while n:
            digit = n % 10
            out += digit ** 2
            n = n // 10
        return out

    def isHappy(self, n: int) -> bool:
        previousOutputs = set()
        while n not in previousOutputs:
            previousOutputs.add(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True
        return False
