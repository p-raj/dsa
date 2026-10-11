class MinHeap:
    
    def __init__(self):
        self.heap = []

    def _bubble_up(self) -> None:
        end = len(self.heap)-1
        while end > 0:
            par = end//2
            A = self.heap
            if A[par] < A[end]:
                return
            A[par], A[end] = A[end], A[par]
            end = par

    def _bubble_down(self, start: int = 0) -> None:
        top = start
        lft = top * 2 + 1
        rgt = top * 2 + 2
        A = self.heap
        if lft < len(A) and A[lft] < A[top]:
            top = lft
        if rgt < len(A) and A[rgt] < A[top]:
            top = rgt
        if top != start:
            A[top], A[start] = A[start], A[top]
            self._bubble_down(start = top)

    def push(self, val: int) -> None:
        self.heap.append(val)
        self._bubble_up()

    def pop(self) -> int:
        if not self.heap:
            return -1
        # swap
        A = self.heap
        A[0], A[len(A)-1] = A[len(A)-1], A[0]
        # pop
        e = A.pop()
        # bubble down
        self._bubble_down()
        return e

    def top(self) -> int:
        return self.heap[0] if self.heap else -1

    def heapify(self, nums: List[int]) -> None:
        n = len(nums)
        i = n//2
        while i >= 0:
            self.min_heapify(nums, i, n)
            i -= 1
        self.heap = nums

    def min_heapify(self, nums, i, n):
        lft = 2 * i
        rgt = 2 * i + 1
        par = i
        # parent should be bigger than
        # both the nodes
        A = nums
        if lft < n and A[lft] < A[par]:
            par = lft
        if rgt < n and A[rgt] < A[par]:
            par = rgt
        
        if par != i:
            A[par], A[i] = A[i], A[par]
            self.min_heapify(A, par, n)
