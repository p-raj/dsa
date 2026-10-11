class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = dict()
        max_ = 0
        pos_ = 0
        pivt = 0
        while pos_ < len(s):
            ch = s[pos_]
            if ch in seen:
                if pos_ - pivt > max_:
                    max_ = pos_ - pivt
                seen[ch] = pos_
                pivt = seen[ch]
                pos_ = pivt
                pos_ += 1
            else:
                seen[ch] = pos_
                pos_ += 1
        if len(s) - pivt > max_:
            max_ = len(s) - pivt
        return max_
