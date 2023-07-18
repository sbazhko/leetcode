# https://leetcode.com/problems/concatenation-of-array/
from typing import List

class Solution:
    # Space O(n + n) ~> O(2n) ~> O(n) 
    # Time O(n)
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(2 * nums)):
            ans.append(nums[i % len(nums)])
        return ans
    
    # Solution 2
    # def getConcatenation(self, nums: List[int]) -> List[int]:
    #     return nums * 2
    
    # Solution 3
    # def getConcatenation(self, nums: List[int]) -> List[int]:
    #     return nums + nums

s = Solution()
print(s.getConcatenation([1,2,3]))
print(s.getConcatenation([1]))
print(s.getConcatenation([]))