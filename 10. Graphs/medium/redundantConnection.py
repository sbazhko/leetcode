# https://leetcode.com/problems/redundant-connection/

from typing import List
import collections


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        connectedNodes = collections.defaultdict(list)

        def findConnection(source, target):
            if source not in seen:
                seen.add(source)
                if source == target:
                    return True
                for neighbour in connectedNodes[source]:
                    # if at least one neigbour is connected to the target -> True
                    if findConnection(neighbour, target):
                        return True
            # no one connected to the target
            return False
        for u, v in edges:
            seen = set()
            # nodes are connected to something, so, there might be a connection between u and v
            if u in connectedNodes and v in connectedNodes and findConnection(u, v):
                return u, v
            connectedNodes[u].append(v)
            connectedNodes[v].append(u)


s = Solution()
assert s.findRedundantConnection(
    [[3, 4], [1, 2], [2, 4], [3, 5], [2, 5]]) == [2, 5]
