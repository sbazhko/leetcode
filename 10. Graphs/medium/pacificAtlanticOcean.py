# https://leetcode.com/problems/pacific-atlantic-water-flow/

from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        atlantic = set()
        pacific = set()

        def dfs(r, c, visited, prevHeight):
            if (r, c) in visited or r not in range(rows) or c not in range(cols) or prevHeight > heights[r][c]:
                return
            visited.add((r, c))
            directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])
            return

        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res
