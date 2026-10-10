# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def maxDepth(node):
            if node is None:
                return False
            left = maxDepth(node.left)
            right = maxDepth(node.right)
            if abs(left - right) > 1:
                self.balanced = False

            return max(left, right) + 1

        maxDepth(root)

        return self.balanced