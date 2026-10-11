from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1_idx = {}
        for idx, c in enumerate(s1):
            if c not in c1_idx:
                c1_idx[c] = []
            c1_idx[c].append(idx) # sorted
        do_check = False
        for ch in s2:
            print(ch, c1_idx)
            if not do_check and ch not in c1_idx:
                continue
            if do_check and ch not in c1_idx:
                return False
            if ch in c1_idx:
                do_check = True
                c1_idx[ch].pop()
                if len(c1_idx[ch]) == 0:
                    c1_idx.pop(ch)
        print(c1_idx)
        return bool(c1_idx)