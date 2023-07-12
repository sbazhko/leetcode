# https://leetcode.com/problems/majority-element/

import math
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elems = {}
        for n in nums:
            if n in elems:
                elems[n] += 1
            else:
                elems[n] = 1
            if elems[n] > math.floor(len(nums) / 2):
                return n

# Wow xd
# def majorityElement(self, nums: List[int]) -> int: # Eg1: nums = [3,2,3] , Eg2: nums = [2,2,1,1,1,2,2]
#         nums = sorted(nums) # Eg1: [2,3,3] , Eg2: [1, 1, 1, 2, 2, 2, 2]
#         return nums[len(nums)//2] # Eg1: 3, Eg2: 2


s = Solution()

print(s.majorityElement([3, 2, 2]))
print(s.majorityElement([3, 3, 2]))
print(s.majorityElement([3, 2]))  # Invalid input by requirements
print(s.majorityElement([2]))
