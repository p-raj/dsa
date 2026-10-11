class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = dict()
        max_ = 0
        pos_ = 0
        pivt = -1
        while pos_ < len(s):
            ch = s[pos_]
            if ch in seen:
                if pos_ - pivt > max_:
                    max_ = pos_ - pivt
                pivt = seen[ch] + 1
                seen[ch] = pos_
                pos_ = pivt
            else:
                seen[ch] = pos_
                pos_ += 1
        if len(s) - pivt > max_:
            max_ = len(s) - pivt
        return max_
