# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        p1 = root1
        p2 = root2
        if p1 == p2 == None:
            return True
        if p1 != None and p2 == None:
            return False
        if p1 == None and p2 != None:
            return False
        if p1.val != p2.val:
            return False
        return (self.flipEquiv(p1.left, p2.left) and self.flipEquiv(p1.right, p2.right)) or (
            self.flipEquiv(p1.left, p2.right) and self.flipEquiv(p1.right, p2.left)
        )

        return False
