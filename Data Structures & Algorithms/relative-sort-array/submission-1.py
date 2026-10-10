class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        H = {}
        for num in arr1:
            if num not in H:
                H[num] = 0
            H[num] += 1
        nxt = 0
        for num in arr2:
            for i in range(nxt, H[num]+nxt):
                arr1[i] = num
            nxt += H[num]
            del(H[num])
        remaining = []
        for k,v in H.items():
            for i in range(nxt, v+nxt):
                remaining.append(k)
        remaining.sort()
        for i in range(len(remaining)):
            arr1[nxt+i] = remaining[i]
        return arr1