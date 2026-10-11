# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        P = pairs
        progress = [P.copy()]
        i = 1
        while i < len(P):
            Pi = P[i]
            j = i - 1
            while j >= 0 and P[j].key > Pi.key:
                P[j + 1] = P[j]
                j -= 1
            P[j + 1] = Pi
            i += 1
            progress.append(P.copy())
        return progress