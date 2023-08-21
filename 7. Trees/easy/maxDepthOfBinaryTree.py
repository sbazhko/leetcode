# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepthDFSRecursive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepthDFSIterative(self, root: Optional[TreeNode]) -> int:
        depth = 0
        stack = [[root, 1]]
        while stack:
            node, currDepth = stack.pop()
            if node:
                stack.append([node.left, currDepth + 1])
                stack.append([node.right, currDepth + 1])
                depth = max(depth, currDepth)
        return depth

    def maxDepthBFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        lvl = 1
        q = deque([root])
        while q:
            # level Xth
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            lvl += 1
        return lvl


tree = TreeNode(4,
                TreeNode(2,
                         TreeNode(1),
                         TreeNode(3)),
                TreeNode(7,
                         TreeNode(6),
                         TreeNode(9)
                         ))
