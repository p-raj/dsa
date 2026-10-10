class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        fnl = [(a[0],a[-1]) for a in arrays]
        A = sorted(fnl, key=lambda x : x[0])
        lft, rgt = 0, len(A)-1
        md = -1
        while lft < rgt:
            md = max(md, abs(A[lft][0]-A[rgt][1]), abs(A[rgt][0]-A[lft][1]))
            if A[lft][1] > A[rgt][1]:
                rgt -= 1
            else:
                lft += 1
        return md