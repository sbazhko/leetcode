# https://leetcode.com/problems/word-search/

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(i, j, wordIdx):
            if len(word) == wordIdx:
                return True
            if (
                i >= len(board) or i < 0 or
                j >= len(board[i]) or j < 0 or
                (i, j) in path or board[i][j] != word[wordIdx]
            ):
                return False
            path.add((i, j))
            res = (
                dfs(i + 1, j, wordIdx + 1) or dfs(i - 1, j, wordIdx + 1) or
                dfs(i, j + 1, wordIdx + 1) or dfs(i, j - 1, wordIdx + 1)
            )
            path.remove((i, j))
            return res

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True
        return False


s = Solution()
assert s.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"],
                ["A", "D", "E", "E"]], "ABCE") == True
