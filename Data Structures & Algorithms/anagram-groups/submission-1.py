from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resp = {}
        for s in strs:
            freqarr = [0] * 26
            freq = Counter(s)
            for c, f in freq.items():
                freqarr[ord(c)-97] = f
            freqarr = tuple(freqarr)
            if freqarr not in resp:
                resp[freqarr] = list()
            resp[freqarr].append(s)
        return list(resp.values())
            

        