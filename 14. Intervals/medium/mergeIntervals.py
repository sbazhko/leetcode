# https://leetcode.com/problems/merge-intervals/

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O (n log n)
        intervals.sort(key=lambda interval: interval[0])
        res = []
        newInterval = intervals[0]
        for i in range(len(intervals)):
            interval = intervals[i]
            if interval[1] < newInterval[0]:
                res.append(interval)
            elif interval[0] > newInterval[1]:
                res.append(newInterval[:])
                newInterval = interval
            else:
                newInterval = [min(interval[0], newInterval[0]),
                               max(interval[1], newInterval[1])]
        res.append(newInterval)
        return res


s = Solution()
s.merge([[1, 3], [2, 6], [8, 10], [15, 18]])
