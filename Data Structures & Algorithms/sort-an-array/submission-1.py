class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        PRIME = 308319771579959250011125575971
        A = nums

        def qs(A, lft, rgt):
            if lft >= rgt:
                return
            pvt = part(A, lft, rgt)
            qs(A, lft, pvt - 1)
            qs(A, pvt + 1, rgt)

        def part(A, lft, rgt):
            size = rgt - lft + 1
            pvt = lft + ((((rgt + lft) // 2) * PRIME) % size)
            A[pvt], A[rgt] = A[rgt], A[pvt]
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

        qs(A, 0, len(A) - 1)
        return A
