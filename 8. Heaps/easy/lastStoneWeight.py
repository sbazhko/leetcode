# https://leetcode.com/problems/last-stone-weight/

from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        invertedStones = [-x for x in stones]
        heapq.heapify(invertedStones)
        while len(invertedStones) > 1:
            stone1 = heapq.heappop(invertedStones)
            stone2 = heapq.heappop(invertedStones)
            collision = abs(stone1 - stone2)
            if collision > 0:
                heapq.heappush(invertedStones, -collision)

        invertedStones.append(0)
        return abs(invertedStones[0])
