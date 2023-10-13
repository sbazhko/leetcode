# https://leetcode.com/problems/non-overlapping-intervals/

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        res = 0
        prevEnd = intervals[0][1]

        for s, e in intervals[1:]:
            if s >= prevEnd:
                # non overlapping left
                # <---prevEnd    s---->
                prevEnd = e
            else:
                res += 1
                prevEnd = min(e, prevEnd)  # assume we keep the shortest
        return res


s = Solution()
s.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]])
s.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]])
s.eraseOverlapIntervals([[1, 2], [2, 3]])
