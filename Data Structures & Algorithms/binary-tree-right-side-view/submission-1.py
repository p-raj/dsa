# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root, h=0):
        if not root:
            return h
        return max(self.height(root.left, h+1), self.height(root.right, h+1))
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        hgt_root = self.height(root)
        hgt_rgt = self.height(root.right)
        hgt_lft = self.height(root.left)
        print(f"{hgt_root=}, {hgt_lft=}, {hgt_rgt=}")

        vis = []
        cur = root
        while cur:
            vis.append(cur.val)
            if cur.right:
                cur = cur.right
            elif cur.left:
                cur = cur.left
            else:
                break

        if hgt_rgt >= hgt_lft:
            return vis

        depth = 1
        cur = root.left
        while cur:
            if depth > hgt_rgt:
                vis.append(cur.val)
            if cur.right:
                cur = cur.right
            elif cur.left:
                cur = cur.left
            else:
                break
            depth += 1

        return vis