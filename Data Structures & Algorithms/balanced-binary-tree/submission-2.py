# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.nh = {}
        self.nh[None] = 0

        def hgt(node):
            if node in self.nh:
                return self.nh[node]
            if not node:
                return 0
            self.nh[node.left] = hgt(node.left)
            self.nh[node.right] = hgt(node.right)
            return 1 + max(self.nh[node.left], self.nh[node.right])
        if not root:
            return True

        return (
            (abs(hgt(root.left) - hgt(root.right)) <= 1)
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
        )
