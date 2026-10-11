class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = dict()
        max_ = 0
        strt = 0
        pivt = strt
        while strt < len(s):
            ch = s[strt]
            if ch in seen:
                pivt = seen[ch]
                if strt - pivt > max_:
                    max_ = strt - pivt
                seen[ch] = strt
                strt = pivt + 1
            else:
                seen[ch] = strt
                strt += 1
        if len(s) - pivt > max_:
            max_ = len(s) - pivt
        return max_
