# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dia = 0
        # return height
        def dfs(node):
            if not node:
                return 0
            lft = dfs(node.left)
            rgt = dfs(node.right)
            self.dia = max(self.dia, lft+rgt)
            return 1 + max(lft, rgt)
        dfs(root)
        return self.dia