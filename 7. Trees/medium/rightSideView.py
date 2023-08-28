# https://leetcode.com/problems/binary-tree-right-side-view/

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightSide = []
        q = deque()
        if root:
            q.append(root)
        while q:
            rightSide.append(q[-1].val)
            for _ in range(len(q)):
                node = q.pop()
                if node.right:
                    q.appendleft(node.right)
                if node.left:
                    q.appendleft(node.left)
        return rightSide


s = Solution()

tree = TreeNode(1, TreeNode(2, TreeNode(5)), TreeNode(3, TreeNode(4)))

s.rightSideView(tree)
