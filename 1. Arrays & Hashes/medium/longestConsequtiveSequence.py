# https://leetcode.com/problems/longest-consecutive-sequence/description/

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen = 0
        currLen = 0
        numsSet = set(nums)
        # find first element in the sequence and extend it while it is consequtive
        for num in numsSet:
            if num - 1 not in numsSet:
                nextNumInSequence = num
                while nextNumInSequence in numsSet:
                    currLen += 1
                    nextNumInSequence += 1
                maxLen = max(currLen, maxLen)
                currLen = 0
        return maxLen


s = Solution()

assert s.longestConsecutive([100, 1, 200, 3, 2, 4]) == 4
assert s.longestConsecutive([1]) == 1
assert s.longestConsecutive([101, 100, 1, 3, 99]) == 3
