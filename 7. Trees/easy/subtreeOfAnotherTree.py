# https://leetcode.com/problems/subtree-of-another-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ? Important notes:
# ? - Binary tree has unique elements
# ? - It makes sense to use properties of binary tree (i.e., use binary search)


class Solution:
    def isSameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)
        return False

    # O(tree * subTree)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


s = Solution()

tree = TreeNode(4,
                TreeNode(7,
                         TreeNode(6),
                         TreeNode(9,
                                  TreeNode(3))
                         ),
                TreeNode(2,
                         TreeNode(1),
                         TreeNode(3))
                )

subTree = TreeNode(2,
                   TreeNode(1),
                   TreeNode(3)
                   )


assert s.isSubtree(tree, subTree) == True
