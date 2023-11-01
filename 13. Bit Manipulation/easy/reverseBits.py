# https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        reversedNumber = 0
        for i in range(32):
            ithBit = (n & (1 << i)) >> i
            reversedNumber = reversedNumber | (ithBit << (31 - i))
        return reversedNumber


s = Solution()
assert s.reverseBits(4) == 1
