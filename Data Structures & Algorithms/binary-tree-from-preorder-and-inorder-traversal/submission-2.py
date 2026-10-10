# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(
        self,
        preorder: List[int],
        inorder: List[int],
    ) -> Optional[TreeNode]:
        root = None
        if not preorder:
            return root
        inorder_map = {k: v for v, k in enumerate(inorder)}
        self.curr_root = 0

        def bt(lft, rgt):
            if lft > rgt:
                return None
            root_val = preorder[self.curr_root]
            root = TreeNode(root_val)
            root_idx = inorder_map[root_val]
            self.curr_root += 1
            root.left = bt(
                lft, root_idx-1
            )
            root.right = bt(
                root_idx+1, rgt
            )
            return root
        
        return bt(0, len(preorder)-1)