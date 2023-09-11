# https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, combination, currSum):
            if currSum == target:
                res.append(combination.copy())
                return
            if i >= len(candidates) or currSum > target:
                return

            combination.append(candidates[i])
            dfs(i, combination, currSum + candidates[i])
            combination.pop()
            dfs(i + 1, combination, currSum)
        dfs(0, [], 0)
        return res
