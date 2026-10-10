# # Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
#     def __repr__(self):
#     	return f"{self.key=} : {self.value=}"

class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self._qs(pairs, 0, len(pairs)-1)
        return pairs
    
    def _qs(self, pairs: List[Pair], lft: int, rgt: int):
        if lft >= rgt:
            return pairs

        pivot = self._p(pairs, lft, rgt)
        # print(f"{pivot=} | {lft=} | {rgt=}")
        self._qs(pairs, lft, pivot-1)
        self._qs(pairs, pivot+1, rgt)

    def _p(self, arr: List[Pair], lft: int, rgt: int) -> int:
        pivot = arr[rgt]
        i = lft  # boundary of < pivot region

        for j in range(lft, rgt):
            if arr[j].key < pivot.key:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i], arr[rgt] = arr[rgt], arr[i]
        return i
    # def _p(self, pairs: List[Pair], lft: int, rgt: int) -> int:
    #     pvt = rgt
    #     pivot = pairs[pvt]
    #     rgt -= 1
    #     while lft <= rgt:
    #         if pairs[lft].key < pivot.key:
    #             lft += 1
    #         else:
    #             pairs[lft], pairs[rgt] = pairs[rgt], pairs[lft]
    #             rgt -= 1
        
        pairs[pvt], pairs[lft] = pairs[lft], pairs[pvt]
        # print(f"{pvt=} | {lft=} | {rgt=} > [ {pairs=} ]")
        return lft

# Solution().quickSort(pairs=[Pair(3, "cat"), Pair(2, "dog"), Pair(3, "bird")])