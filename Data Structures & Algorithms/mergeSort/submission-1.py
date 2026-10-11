# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def pprint(self, pairs):
        print([(p.key, p.value) for p in pairs])

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self._ms(pairs, 0, len(pairs)-1)
    
    def _ms(self, pairs, lft, rgt):
        if lft >= rgt:
            return pairs

        mid = (lft + rgt)//2
        self._ms(pairs, lft, mid)
        self._ms(pairs, mid+1, rgt)
        self._m(pairs, lft, mid, rgt)
        return pairs
    
    def _m(self, pairs, lft, mid, rgt):
        A = pairs
        L = pairs[lft: mid+1]
        R = pairs[mid+1:rgt+1]
        i = 0
        j = 0
        k = lft
        while i < len(L) and j < len(R):
            if L[i].key == R[j].key:
                A[k] = L[i]
                i += 1
                k += 1
                A[k] = R[j]
                j += 1
                k += 1
            else:
                if L[i].key < R[j].key:
                    A[k] = L[i]
                    i += 1
                else:
                    A[k] = R[j]
                    j += 1
                k += 1
        
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1
        # self.pprint(A)
        