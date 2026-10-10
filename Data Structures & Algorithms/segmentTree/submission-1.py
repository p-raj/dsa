class Node:
    def __init__(self, sum_: int, lft: int, rgt: int):
        self.sum_: int = sum_
        self.lft_: Node | None = None
        self.rgt_: Node | None = None
        self.lft: int = lft
        self.rgt: int = rgt


class SegmentTree:
    def __init__(self, nums: List[int]):
        self.root = self._build(nums, 0, len(nums) - 1)

    def _build(self, nums: List[int], lft: int, rgt: int):
        if lft == rgt:
            return Node(nums[lft], lft, rgt)
        mid = (lft + rgt) // 2
        root = Node(0, lft, rgt)
        root.lft_ = self._build(nums, lft, mid)
        root.rgt_ = self._build(nums, mid + 1, rgt)
        root.sum_ = root.lft_.sum_ + root.rgt_.sum_
        return root

    def update(self, index: int, val: int) -> None:
        self._update(self.root, index, val)

    def _update(self, root, idx, val):
        if root.lft == root.rgt:
            root.sum_ = val
            return
        mid = (root.lft + root.rgt) // 2
        if idx <= mid:
            self._update(root.lft_, idx, val)
        else:
            self._update(root.rgt_, idx, val)
        root.sum_ = root.lft_.sum_ + root.rgt_.sum_

    def query(self, L: int, R: int) -> int:
        return self._query(self.root, L, R)

    def _query(self, root, lft, rgt):
        if lft <= root.lft and root.rgt <= rgt:
            return root.sum_

        if rgt < root.lft or lft > root.rgt:
            return 0

        return self._query(root.lft_, lft, rgt) + self._query(root.rgt_, lft, rgt)
