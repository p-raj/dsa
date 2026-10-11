from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return t

        tfreq = defaultdict(int)
        for c in t:
            tfreq[c] += 1
        
        wfreq = defaultdict(int)
        wrange = [-1,-1]
        wlenth = float("infinity")
        matched = 0
        lft = 0
        rgt = 0
        while rgt < len(s):
            wfreq[s[rgt]] += 1
            if s[rgt] in tfreq and wfreq[s[rgt]] == tfreq[s[rgt]]:
                matched += 1
            
            while matched == len(t):
                if (rgt-lft+1) < wlenth:
                    wlenth = rgt-lft+1
                    wrange = [lft, rgt]
                
                # shrink
                wfreq[s[lft]] -= 1
                if s[lft] in tfreq and wfreq[s[lft]] < tfreq[s[lft]]:
                    matched -= 1
                lft += 1
            rgt += 1
        lft, rgt = wrange
        return s[lft: rgt+1] if wlenth != float("infinity") else ""
