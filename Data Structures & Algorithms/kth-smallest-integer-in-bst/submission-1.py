# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Morris Traversal
        curr = root
        while curr:
            if curr.left:
                # find predecessor
                # left most node in the right tree?
                pred = curr.left
                while pred.right and pred.right != curr:
                    # pred.right != curr means the right
                    # is linked back
                    # we have already traced this
                    pred = pred.right
                if not pred.right:
                    pred.right = curr #<- back to the future
                    curr = curr.left
                else:
                    pred.right = None #<- delink
                    k -= 1
                    if k == 0:
                        return curr.val
                    curr = curr.right
            else:
                k -= 1
                if k == 0:
                    return curr.val
                curr = curr.right #<- back to the future