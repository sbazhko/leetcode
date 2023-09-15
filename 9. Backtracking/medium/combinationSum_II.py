# https://leetcode.com/problems/combination-sum-ii/description/

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, combinations, currSum):
            if currSum == target:
                res.append(combinations.copy())
                return
            if currSum > target or i == len(candidates):
                return

            combinations.append(candidates[i])
            dfs(i + 1, combinations, currSum + candidates[i])
            combinations.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, combinations, currSum)
        dfs(0, [], 0)
        return res


s = Solution()
s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
