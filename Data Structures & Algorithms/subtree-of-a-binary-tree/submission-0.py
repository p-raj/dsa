# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and subRoot or not subRoot and root:
            return False
        if subRoot == root == None :
            return True
        if root.val == subRoot.val:
            return self.isSubtree(root.left, subRoot.left) and self.isSubtree(
                root.right, subRoot.right
            )
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
