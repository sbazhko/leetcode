# https://leetcode.com/problems/kth-largest-element-in-a-stream/

import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap, self.k = nums, k
        heapq.heapify(nums)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
kthLargest = KthLargest(3, [4, 5, 8, 2])
assert kthLargest.add(3) == 4
assert kthLargest.add(5) == 5
assert kthLargest.add(10) == 5
assert kthLargest.add(9) == 8
assert kthLargest.add(4) == 8
