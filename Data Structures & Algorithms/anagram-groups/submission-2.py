from collections import Counter
from typing import List

class Solution:
    def char_range(self, c1, c2):
        for c in range(ord(c1), ord(c2) + 1):
            yield chr(c)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cdrift = ord('a')
        ndrift = ord('0')
        soln = {}
        
        for s in strs:
            # 1. Create the base mutable bytearray template
            tmplt = bytearray("".join(f"{c}0000" for c in self.char_range("a", "z")), encoding="utf-8")
            f = Counter(s)
            
            for ch, co in f.items():
                idx = (ord(ch) - cdrift) * 5
                num = f'{co:04}'
                for i, n in enumerate(num):
                    print(ord(n) - ndrift, n)
                    tmplt[idx+1+i] = ord(n) - ndrift
            
            # Convert bytearray to immutable bytes so it can be a dict key
            key = bytes(tmplt) 
            if key not in soln:
                soln[key] = []
            soln[key].append(s)
            
        return list(soln.values())
