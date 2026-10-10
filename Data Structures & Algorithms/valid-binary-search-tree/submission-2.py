# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.nodes = []

        def trace(root):
            if not root:
                return
            trace(root.left)
            self.nodes.append(root.val)
            trace(root.right)
        trace(root)
        print(self.nodes)
        lft = 0
        rgt = 1
        while rgt < len(self.nodes):
            if self.nodes[lft] >= self.nodes[rgt]:
                return False
            lft += 1
            rgt += 1
        return True