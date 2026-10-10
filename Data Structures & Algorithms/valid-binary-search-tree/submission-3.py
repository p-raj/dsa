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

        def is_valid(root, min_, max_):
            if not root:
                return True
            return (
                min_ < root.val < max_
                and is_valid(root.left, min_, root.val)
                and is_valid(root.right, root.val, max_)
            )

        return is_valid(root, float("-inf"), float("inf"))
