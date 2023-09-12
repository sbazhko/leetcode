# https://leetcode.com/problems/permutations/

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(used, permutation):
            if len(nums) == len(permutation):
                res.append(permutation[:])
                return
            for k in range(len(nums)):
                # don't use K down the path
                if used[k]:
                    continue

                permutation.append(nums[k])
                used[k] = True
                dfs(used, permutation)

                # make unused in other paths (next K in the loop)
                permutation.pop()
                used[k] = False
        dfs([False] * len(nums), [])
        return res


s = Solution()
s.permute([1, 2, 3])
