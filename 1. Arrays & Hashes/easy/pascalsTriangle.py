# https://leetcode.com/problems/pascals-triangle/

from typing import List


class Solution:
    # Time O(n^2) Space O(n)
    # def generate(self, numRows: int) -> List[List[int]]:
    #     pascalsTriangle = [[1]]
    #     prevRow = []
    #     for i in range(1, numRows):
    #         currRow = [1]
    #         for j in range(i - 1):
    #             leftEl = prevRow[j] + prevRow[j + 1]
    #             currRow.append(leftEl)
    #         currRow.append(1)
    #         prevRow = currRow
    #         pascalsTriangle.append(currRow)
    #     return pascalsTriangle

    def generate(self, numRows: int) -> List[List[int]]:
        pascalsTriangle = [[1]]
        for i in range(numRows - 1):
            prevRow = [0] + pascalsTriangle[-1] + [0]
            currRow = []
            for j in range(len(pascalsTriangle[-1]) + 1):
                currRow.append(prevRow[j] + prevRow[j + 1])
            pascalsTriangle.append(currRow)
        return pascalsTriangle

s = Solution()
print(s.generate(1))
print(s.generate(2))
print(s.generate(3))
print(s.generate(4))
print(s.generate(5))