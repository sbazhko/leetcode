# https://leetcode.com/problems/plus-one/

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        digits[len(digits) - 1] += 1
        for i in range(len(digits) - 1, -1, -1):
            tmp = digits[i] + carry
            digits[i] = tmp % 10
            carry = tmp // 10
        return [1] + digits if carry else digits
    
s = Solution()
assert s.plusOne([8, 9, 9]) == [9, 0, 0]
assert s.plusOne([9]) == [1, 0]