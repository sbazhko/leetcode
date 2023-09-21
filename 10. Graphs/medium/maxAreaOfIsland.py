# https://leetcode.com/problems/max-area-of-island/

from typing import Optional


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxSquare = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or (r, c) in visited or grid[r][c] == 0:
                return 0

            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            res = 1
            visited.add((r, c))
            for dr, dc in directions:
                res += dfs(r + dr, c + dc)
            return res

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    currMax = dfs(r, c)
                    maxSquare = max(currMax, maxSquare)
        return maxSquare


s = Solution()

grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [
    0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
assert s.maxAreaOfIsland(grid) == 6
