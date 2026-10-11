# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        lft = root.left
        rgt = root.right
        if (lft and lft.val >= root.val) or (rgt and rgt.val <= root.val):
            return False
        return self.isValidBST(lft) and self.isValidBST(rgt)