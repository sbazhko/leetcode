# https://leetcode.com/problems/3sum/description/

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        j = len(nums) - 1
        k = i + 1
        triplets = []
        nums.sort()
        while i < len(nums) - 1:
            while i < j and nums[i] == nums[i+1]:
                i += 1
            while k < j:
                sum = nums[i] + nums[j] + nums[k]
                if sum > 0:
                    j -= 1
                elif sum < 0:
                    k += 1
                else:
                    triplets.append([nums[i], nums[j], nums[k]])
                    k += 1  # [0, 1, 1, 2, 3]
                    while k < j and nums[k] == nums[k - 1]:
                        k += 1
            j = len(nums) - 1
            i += 1
            k = i + 1
        return triplets


s = Solution()

print(s.threeSum([0, 0, 0]))
print(s.threeSum([0, 0, 0, 0]))
print(s.threeSum([0, 1, 1]))
print(s.threeSum([-1, 0, 1, 2, -1, -4]))  # [-4, -1, -1, 0, 1, 2]
print(s.threeSum([-2, 0, 1, 1, 2]))
print(s.threeSum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]))
