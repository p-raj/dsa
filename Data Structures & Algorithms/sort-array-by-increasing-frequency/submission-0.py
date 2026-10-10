from collections import Counter


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        NC = Counter(nums)
        D = {}
        for k, v in NC.items():
            if v not in D:
                D[v] = list()
            D[v].append(k)
        del NC
        D = dict(sorted(D.items(), key=lambda i: i[0]))
        res = []
        for k, arr in D.items():
            arr = arr * k
            (arr).sort(reverse=True)
            res += arr
        return res
