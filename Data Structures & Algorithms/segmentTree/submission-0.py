class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self.nums = nums
    
    def update(self, index: int, val: int) -> None:
        self.nums[index] = val
    
    def query(self, L: int, R: int) -> int:
        return sum(self.nums[L:R+1])
