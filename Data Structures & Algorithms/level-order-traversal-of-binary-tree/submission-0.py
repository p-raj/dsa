# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = {}
        def trace(root, depth=0):
            if not root:
                return
            if depth not in self.res:
                self.res[depth] = list()
            self.res[depth].append(root.val)
            trace(root.left, depth+1)
            trace(root.right, depth+1)
        
        trace(root)
        return list(self.res.values())