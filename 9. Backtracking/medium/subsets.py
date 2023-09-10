# https://leetcode.com/problems/subsets/

# O(n * 2 ^ n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return result


s = Solution()
s.subsets([1, 2, 3])
