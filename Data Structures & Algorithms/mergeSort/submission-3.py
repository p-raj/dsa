# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def pprint(self, pairs):
        print([(p.key, p.value) for p in pairs])

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        aux = [None] * len(pairs)
        return self._ms(pairs, aux, 0, len(pairs)-1)
    
    def _ms(self, pairs, aux, lft, rgt):
        if lft >= rgt:
            return pairs

        mid = (lft + rgt)//2
        self._ms(pairs, aux, lft, mid)
        self._ms(pairs, aux, mid+1, rgt)
        self._m(pairs, aux, lft, mid, rgt)
        return pairs
    
    def _m(self, pairs, aux, lft, mid, rgt):
        A = pairs
        for a in range(lft, rgt+1):
            aux[a] = A[a]
        i = lft
        j = mid + 1
        k = lft
        while i <= mid and j <= rgt:
            if aux[i].key <= aux[j].key:
                A[k] = aux[i]
                i += 1
            else:
                A[k] = aux[j]
                j += 1
            k += 1
        
        while i <= mid:
            A[k] = aux[i]
            i += 1
            k += 1
        
        while j <= rgt:
            A[k] = aux[j]
            j += 1
            k += 1
        # self.pprint(A)
        