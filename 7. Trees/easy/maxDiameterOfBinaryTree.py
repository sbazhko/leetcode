# https://leetcode.com/problems/diameter-of-binary-tree/

from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]

        def dfs(root):
            if not root:
                return 0
            heightL = dfs(root.left)
            heightR = dfs(root.right)
            # this calculation is done before adding the root node to the height
            # otherwise root would be "double included"
            diameter[0] = max(heightL + heightR, diameter[0])
            return 1 + max(heightL, heightR)
        dfs(root)
        return diameter[0]


tree = TreeNode(4,
                TreeNode(2,
                         TreeNode(1),
                         TreeNode(3)),
                TreeNode(7,
                         TreeNode(6),
                         TreeNode(9,
                                  TreeNode(3))
                         ))
s = Solution()
s.diameterOfBinaryTree(tree)
