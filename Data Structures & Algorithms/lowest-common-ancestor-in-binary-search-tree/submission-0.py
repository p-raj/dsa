# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def track_parents(self, root: TreeNode) -> list[tuple[int, TreeNode]]:
        vals = []
        if not root:
            return vals
        while root:
            vals.append((root.val, root))
            root = self.paren[root.val]
        return vals
        
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.paren = {}

        def trace(root, par=None):
            if not root:
                return
            if root.val not in self.paren:
                self.paren[root.val] = None
            if par:
                self.paren[root.val] = par
            trace(root.left, root)
            trace(root.right, root)
        trace(root, None)
        ppar = self.track_parents(p)
        qpar = self.track_parents(q)
        last_match = None
        while qpar and ppar:
            pp = ppar.pop()
            pq = qpar.pop()
            if pp[0] == pq[0]:
                last_match = pp[1]
        return last_match

