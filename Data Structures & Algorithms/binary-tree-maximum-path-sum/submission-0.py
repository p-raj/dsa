# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(
            sum([root.val, self.maxPathSum(root.left), self.maxPathSum(root.right)]),
            sum([root.val, self.maxPathSum(root.left)]),
            sum([root.val, self.maxPathSum(root.right)]),
            self.maxPathSum(root.left),
            self.maxPathSum(root.right),
        )
