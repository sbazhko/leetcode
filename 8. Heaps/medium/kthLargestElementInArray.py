# https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = nums
        heapq.heapify(minHeap)
        while len(minHeap) > k:
            heapq.heappop(minHeap)
        return minHeap[0]

# TODO: solution with quickSelect
