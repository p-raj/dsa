from collections import Counter
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        d = Counter(s)
        # return sum(d.values()) % 2 == len(s) % 2
        r = dict()
        for k, v in d.items():
            if v % 2 == 0:
                continue
            r[k] = v
        print(r,len(r.keys()) )
        return len(r.keys()) < 2
        