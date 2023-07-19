# https://leetcode.com/problems/top-k-frequent-elements/

# Constrains: must be better than O(n log n)
#             It is guaranteed that the answer is unique.

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        # each index is a count which has a list of nums that have index number of occurences
        ascendingCounts = [[] for i in range(len(nums) + 1)]
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        for n, c in counts.items():
            ascendingCounts[c].append(n)

        topKFrequences = []
        for i in range(len(ascendingCounts) - 1, -1, -1):
            if ascendingCounts[i]:
                for j in range(0, len(ascendingCounts[i])):
                    topKFrequences.append(ascendingCounts[i][j])
                    if len(topKFrequences) == k:
                        return topKFrequences


s = Solution()

print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(s.topKFrequent([1], 1))
