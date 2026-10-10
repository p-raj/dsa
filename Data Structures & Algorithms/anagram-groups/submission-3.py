from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        soln = defaultdict(list)
        drift = ord('a')
        for s in strs:
            n = [0] * 26
            for c in s:
                n[ord(c) - drift] += 1
            
            soln[tuple(n)].append(s)
        
        return list(soln.values())
