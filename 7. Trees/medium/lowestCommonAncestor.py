# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    # O(log n)
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        while curr:
            if q.val > curr.val and p.val > curr.val:
                curr = curr.right
            elif q.val < curr.val and p.val < curr.val:
                curr = curr.left
            else:
                return curr


s = Solution()

tree = TreeNode(4,
                TreeNode(2,
                         TreeNode(1),
                         TreeNode(3)),
                TreeNode(7,
                         TreeNode(6),
                         TreeNode(9,
                                  TreeNode(3))
                         ))

s.lowestCommonAncestor(tree, tree.left.left, tree.left.right)
