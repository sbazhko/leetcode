# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # TODO: iterative solution
    def kthSmallestRecursive(self, root: Optional[TreeNode], k: int) -> int:
        inOrderElements = []

        def dfsInOrder(root):
            if not root:
                return None
            dfsInOrder(root.left)
            inOrderElements.append(root.val)
            dfsInOrder(root.right)
        dfsInOrder(root)
        return inOrderElements[k - 1]


s = Solution()

s.kthSmallest(root, 4)
