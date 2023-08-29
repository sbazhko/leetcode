# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, currMax):
            if not root:
                return 0
            res = 1 if root.val >= currMax else 0
            res += dfs(root.left, max(currMax, root.val))
            res += dfs(root.right, max(currMax, root.val))
            return res
        return dfs(root, root.val)


s = Solution()

tree = TreeNode(3,
                TreeNode(1,
                         TreeNode(3), None),
                TreeNode(4,
                         TreeNode(1),
                         TreeNode(5, None)))

s.goodNodes(tree)
