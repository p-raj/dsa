# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # dfs_po:
        # if root:
        # root.val
        # dfs_po(root.left)
        # dfs_po(root.right)

        # dfs_io:
        # if root:
        # dfs_io(root.left)
        # root.val
        # dfs_io(root.right)

        # po gives us the roots in sequence
        # io gives the divison of [lft]<-R->[rgt]

        root = None
        if not preorder:
            return root
        root_val = preorder[0]
        root = TreeNode(root_val)
        if len (preorder) == 1:
            return root
        # print("1] ", preorder, inorder)
        root_io_idx = inorder.index(root_val)
        left_io_tree = inorder[:root_io_idx]
        right_io_tree = inorder[root_io_idx+1:]

        # print("2] ", left_io_tree, right_io_tree )
        if len(left_io_tree):
            # print("<3] ", preorder[1:len(left_io_tree)])
            root.left = self.buildTree(
                preorder[1:len(left_io_tree)+1]
                ,left_io_tree
            )
        if len(right_io_tree):
            # print("<4] ", preorder[len(left_io_tree)+1:])
            root.right = self.buildTree(
                preorder[len(left_io_tree)+1:]
                ,right_io_tree
            )
        return root
