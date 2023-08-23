# https://leetcode.com/problems/balanced-binary-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # O(n)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]

        def dfs(root):
            if not root:
                return 0
            heightL = dfs(root.left)
            heightR = dfs(root.right)
            if abs(heightL - heightR) > 1:
                balanced[0] = False
            return 1 + max(heightL, heightR)
        dfs(root)
        return balanced[0]


s = Solution()

tree = TreeNode(4,
                TreeNode(2,
                         TreeNode(1),
                         TreeNode(3)),
                TreeNode(7,
                         TreeNode(6),
                         TreeNode(9)
                         ))
tree2 = TreeNode(4,
                 TreeNode(2,
                          TreeNode(1),
                          TreeNode(3)),
                 TreeNode(7,
                          None,
                          TreeNode(9,
                                   TreeNode(3))
                          ))
assert s.isBalanced(tree) == True
assert s.isBalanced(tree2) == False
