# https://leetcode.com/problems/search-a-2d-matrix/

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, (len(matrix[0]) * len(matrix)) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            mrow = m // len(matrix[0])
            mcol = m % len(matrix[0])
            el = matrix[mrow][mcol]
            if target == el:
                return True
            elif target > el:
                l = m + 1
            else:
                r = m - 1
        return False


s = Solution()

assert s.searchMatrix(
    matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3) == True

assert s.searchMatrix(
    matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13) == False
