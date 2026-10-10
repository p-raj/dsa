# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0

        def count_g(root, par=None, mval=None):
            if not root:
                return
            rgt = root.right
            lft = root.left
            if (not mval) or (mval and mval <= root.val):
                mval = root.val
                self.good += 1
            count_g(lft, root, mval)
            count_g(rgt, root, mval)

        count_g(root)
        return self.good
