# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 1

        def count_g(root, par=None):
            if not root:
                return
            print(root.val)
            rgt = root.right
            lft = root.left
            if par and root.val >= par.val:
                self.good += 1
            if not par:
                count_g(lft, root)
                count_g(rgt, root)
            else:
                if rgt and rgt.val > root.val:
                    count_g(rgt, root)
                if lft and lft.val > root.val:
                    count_g(lft, root)
                
        count_g(root, None)
        return self.good
