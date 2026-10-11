# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def to_str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        return self.to_str(root.left) + str(root.val) + self.to_str(root.right)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        r = self.to_str(root)
        rs = self.to_str(subRoot)
        return r.startswith(rs) or r.endswith(rs)