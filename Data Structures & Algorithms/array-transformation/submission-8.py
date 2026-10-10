class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        changed = True

        while changed:
            changed = False
            p = arr[0]
            for i in range(1, len(arr) - 1):
                t = arr[i]

                if arr[i] > p and arr[i] > arr[i + 1]:
                    arr[i] -= 1
                    changed = True
                elif arr[i] < p and arr[i] < arr[i + 1]:
                    arr[i] += 1
                    changed = True

                p = t

        return arr
