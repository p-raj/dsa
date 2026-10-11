class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pos = 0
        pivot = 0
        seen = dict()
        max_ = 0
        while pos < len(s):
            ch = s[pos]
            if ch in seen:
                delta = pos - seen[ch]
                if delta > max_:
                    max_ = delta
                pivot = seen[ch]
                pos, seen[ch] = seen[ch] + 1, pos
            else:
                pos, seen[ch] = pos + 1, pos
        
        delta = pos - pivot
        if delta > max_:
            max_ = delta

        return max_