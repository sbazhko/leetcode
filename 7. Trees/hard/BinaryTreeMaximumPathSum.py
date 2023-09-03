# https://leetcode.com/problems/binary-tree-maximum-path-sum/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            # use max(.., 0) to not count branches with negative returns
            leftMax = max(0, leftMax)
            rightMax = max(0, rightMax)
            # compute path with counting split at the current root position:
            res[0] = max(res[0], root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax)
        dfs(root)
        return res[0]
