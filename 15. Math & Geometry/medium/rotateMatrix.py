# https://leetcode.com/problems/rotate-image/

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1
        while l < r:
            # number of rotations
            for i in range(l - r):
                top, bottom = l, r

                # save top left value
                topLeft = matrix[top][l + i]

                # move bottom left into top-left
                matrix[top][l + i] = matrix[bottom - i][l]
                # move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]
                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]
                # move top left into top right
                matrix[top + i][r] = topLeft
            l += 1
            r -= 1


matrix = [[5, 1, 9, 11], [2, 4, 8, 10],
          [13, 3, 6, 7], [15, 14, 12, 16]]
s = Solution()
print(matrix)
s.rotate(matrix)
print(matrix)
