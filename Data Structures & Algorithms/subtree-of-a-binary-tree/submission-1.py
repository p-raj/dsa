class Solution:
    def isSameTree(self, a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        if a.val != b.val:
            return False

        return (
            self.isSameTree(a.left, b.left)
            and self.isSameTree(a.right, b.right)
        )

    def isSubtree(self, root, subRoot):
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return (
            self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )