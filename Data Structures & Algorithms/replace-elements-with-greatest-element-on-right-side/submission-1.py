class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        elem = -1
        rgt = len(arr) - 1
        while rgt >= 0:
            if elem < 0:
                elem = arr[rgt]
                arr[rgt] = -1
            else:
                t = arr[rgt]
                arr[rgt] = elem
                elem = max(t, elem)
            rgt -= 1
        return arr