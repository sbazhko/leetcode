# https://leetcode.com/problems/k-closest-points-to-origin/

from typing import List
import heapq
import math


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        heapq.heapify(distances)
        for p in points:
            distance = math.sqrt(pow(p[0] - 0, 2) + pow(p[1] - 0, 2))
            heapq.heappush(distances, (distance, p))
        kClosest = []
        while k:
            kClosest.append(heapq.heappop(distances)[1])
            k -= 1
        return kClosest


s = Solution()
assert s.kClosest([[1, 3], [-2, 2]], 1) == [[-2, 2]]
