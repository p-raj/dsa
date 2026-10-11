class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        # o-n
        for idx, s in enumerate(strs):
            strs[idx] = max(s, s[::-1])
        # o-n.lg.n
        s = "".join(strs)
        s = [c for c in s]
        #eg = "abcba.abcba.abcba.abdba"
        
        max_ = -1
        for c in s:
            max_ = max(max_, ord(c))
        peaks = [i for i,c in enumerate(s) if ord(c) == max_]
        chunks_bw_peaks = []
        lft = 0
        for rgt in peaks:
            chunks_bw_peaks.append(s[lft: rgt])
            lft = rgt
        chunks_bw_peaks.append(s[rgt:])
        res = []
        for c in chunks_bw_peaks:
            res.append("".join(c))
        s = "".join(sorted(res, reverse=True))
        return "".join(s)
