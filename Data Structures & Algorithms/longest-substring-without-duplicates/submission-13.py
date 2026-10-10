class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = dict()
        max_ = 0
        pos = 0
        pivt = 0
        while pos < len(s):            
            ch = s[pos]
            if ch in seen:
                pivt = max(seen[ch] + 1, pivt)
            seen[ch] = pos
            max_ = max(max_, pos - pivt + 1)
            pos += 1
        return max_