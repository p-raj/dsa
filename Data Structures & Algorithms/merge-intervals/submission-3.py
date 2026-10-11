class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals.sort()

        def m(A, lft: int, rgt: int):
            print(A[lft:rgt])
            if rgt - lft < 0:
                return []
            if rgt - lft == 0:
                return [A[lft]]
            if rgt - lft == 1:
                L = A[lft]
                R = A[rgt]
                if L[1] < R[0]:
                    return [L, R]
                elif L[0] > R[1]:
                    return [R, L]
                elif L[0] <= R[0] and L[1] <= R[1]:
                    return [[L[0], R[1]]]
                elif L[0] <= R[0] and L[1] > R[1]:
                    return [[L[0], L[1]]]
                elif L[0] > R[0] and L[1] > R[1]:
                    return [[R[0], L[1]]]
                else:
                    raise Exception(f"Nope : {L=} & {R=}")
            mid = (rgt + lft)//2
            LEFT = m(A, lft, mid)
            RIGT = m(A, mid+1, rgt)
            res = LEFT[:]
            for r in RIGT:
                L = res[-1]
                R = r
                if L[1] < R[0]:
                    res.append(R)
                else:
                    res[-1] = [L[0], max(L[1], R[1])]
            return res

        res = m(intervals, 0, len(intervals)-1)
        return res
