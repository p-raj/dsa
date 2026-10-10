class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        anr = [0] * len(arr)
        elem = -1
        for i in range(len(arr)-1, -1, -1):
            anr[i] = elem
            elem = max(elem, arr[i])
        return anr