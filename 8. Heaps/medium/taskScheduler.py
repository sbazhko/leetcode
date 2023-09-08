# https://leetcode.com/problems/task-scheduler/

from typing import List
from collections import Counter, deque
import heapq


class Solution:
    # O(n * idles)
    # Intuition: we have to always process the most frequent task first, so that it can be put on cooldown as soon as possible
    def leastInterval(self, tasks: List[str], cooldown: int) -> int:
        tasks = Counter(tasks)
        maxHeap = [-cnt for cnt in tasks.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + cooldown])
            if q and time == q[0][1]:
                cnt, _ = q.popleft()
                heapq.heappush(maxHeap, cnt)

        return time
