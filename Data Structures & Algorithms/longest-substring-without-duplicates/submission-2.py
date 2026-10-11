class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = dict()
        max_ = 0
        strt = 0
        while strt < len(s):
            ch = s[strt]
            if ch in seen:
                idx = seen[ch]
                if strt - idx > max_:
                    max_ = strt - idx
                seen[ch] = strt
                strt = idx + 1
            else:
                seen[ch] = strt
                strt += 1
        return max_
