from collections import Counter


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            clft = Counter(nums[0:i])
            clft = dict(sorted(clft.items(), key=lambda i: i[1], reverse=True))
            crgt = Counter(nums[i:])
            crgt = dict(sorted(crgt.items(), key=lambda i: i[1], reverse=True))
            klft = next(iter(clft), None)
            krgt = next(iter(crgt), None)
            if klft is not None and krgt is not None:
                vlft = clft[klft]
                vrgt = crgt[krgt]
                if 2 * vlft > i and 2 * vrgt > (len(nums) - i) and klft == krgt:
                    return i - 1
        return -1
