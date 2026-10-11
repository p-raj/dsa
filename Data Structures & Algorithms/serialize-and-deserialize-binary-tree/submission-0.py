# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
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
    # Encodes a tree to a single string.

    def po(self, root: Optional[TreeNode]) -> str:
        pos = ""
        def dfs(root):
            nonlocal pos
            if not root:
                return ""
            pos += str(root.val)
            pos += ","
            dfs(root.left)
            dfs(root.right)
        pos += ""
        dfs(root)
        return pos

    def io(self, root: Optional[TreeNode]) -> str:
        ios = ""
        def dfs(root):
            nonlocal ios
            if not root:
                return ""
            dfs(root.left)
            ios += str(root.val)
            ios += ","
            dfs(root.right)
        ios += ""
        dfs(root)
        return ios

    def serialize(self, root: Optional[TreeNode]) -> str:
        pos = self.po(root)
        ios = self.io(root)
        return pos + "#" + ios
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        pos, ios = data.split("#")
        pos = list(map(int, filter(lambda x: x, pos.split(","))))
        ios = list(map(int, filter(lambda x: x, ios.split(","))))
        return self.buildTree(pos, ios)