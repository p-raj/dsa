import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        L = nums1
        R = nums2
        if len(L) > len(R):
            R, L = L, R
        
        # median {M} would be at (len(L) + len(R))//2
        # half the elements would be smaller than {M}
        # lft ptr in L
        # rgt ptr in R
        # such that L[0:lft]+R[0:rgt] < {M}
        mid = (len(L) + len(R))//2
        #-------------------
        # partitioning algo
        # [....AL|AR__]
        # [...BL|BR___]
        #-------------------
        l,r = 0, len(L) - 1
        inf = math.inf
        is_odd = (len(L) + len(R)) % 2 == 1
        while True:
            ax = (l+r)//2
            bx = mid - ax - 2
            LL = L[ax] if ax >= 0 else -inf
            LR = L[ax+1] if ax+1 < len(L) else inf
            RL = R[bx] if bx >= 0 else -inf
            RR = R[bx+1] if bx + 1 < len(R) else inf

            if LL <= RR and RL <= LR:
                if is_odd:
                    return min(LR, RR)
                return (max(LL, RL) + min(LR, RR))/2
            elif LL > RR:
                r = ax - 1
            else:
                l = ax + 1

