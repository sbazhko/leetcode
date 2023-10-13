# https://leetcode.com/problems/insert-interval/

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval[0], newInterval[1]
        res = []
        for i in range(len(intervals)):
            if end < intervals[i][0]:  # end new Interval < start of interval
                res.append(newInterval)
                return res + intervals[i:]
            elif start > intervals[i][1]:  # non overlapping at right
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(
                    newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res


s = Solution()
s.insert(intervals=[[1, 5]], newInterval=[6, 8])
s.insert(intervals=[[1, 5]], newInterval=[5, 7])
s.insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5])
s.insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]
         )
