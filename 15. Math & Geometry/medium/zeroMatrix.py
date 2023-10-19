# https://leetcode.com/problems/set-matrix-zeroes/

from typing import List


class Solution:
    # TODO: solve with row+col+cell
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    # write to all non zero cells in this row and col T
                    for k in range(len(matrix[i])):
                        if matrix[i][k] != 0:
                            matrix[i][k] = 'T'
                    for n in range(len(matrix)):
                        if matrix[n][j] != 0:
                            matrix[n][j] = 'T'

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "T":
                    matrix[i][j] = 0
        return


s = Solution()
s.setZeroes(matrix=[[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
