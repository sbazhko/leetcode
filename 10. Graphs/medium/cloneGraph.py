# https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def clone(node):
            if not node:
                return
            if node in oldToNew:
                return oldToNew[node]

            newNode = Node(node.val)
            oldToNew[node] = newNode
            for neighbor in node.neighbors:
                newNode.neighbors.append(clone(neighbor))
            return newNode
        return clone(node)


s = Solution()
s.cloneGraph([[2, 4], [1, 3], [2, 4], [1, 3]])
