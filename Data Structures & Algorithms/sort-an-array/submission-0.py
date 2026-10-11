class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        A = nums

        def qs(A, lft, rgt):
            if lft >= rgt:
                return
            pvt = part(A, lft, rgt)
            qs(A, lft, pvt-1)
            qs(A, pvt+1, rgt)
        
        def part(A, lft, rgt):
            pvt = rgt
            rgt -= 1
            while lft <= rgt:
                if A[lft] > A[pvt]:
                    A[lft], A[rgt] = A[rgt], A[lft]
                    rgt -= 1
                else:
                    lft += 1
            A[lft], A[pvt] = A[pvt], A[lft]
            pvt = lft
            return pvt

        qs(A, 0, len(A)-1)
        return A