class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        count = 0
        mc = 0
        for ch in s:
            if ch not in seen:
                seen.add(ch)
                count += 1
            else:
                if count > mc:
                    mc = count
                seen = set()
                seen.add(ch)
                count = 1
        return mc