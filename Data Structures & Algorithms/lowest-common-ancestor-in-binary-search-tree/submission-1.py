# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root
        if p.val > cur.val > q.val or p.val < cur.val < q.val:
            return cur
        if p.val > cur.val and q.val > cur.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if p.val < cur.val and q.val < cur.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val == cur.val:
            return p
        if q.val == cur.val:
            return q
