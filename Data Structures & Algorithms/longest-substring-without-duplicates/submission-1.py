class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        count = 0
        mc = 0
        for ch in s:
            if ch in seen:
                if count > mc:
                    mc = count
                seen = set()
                seen.add(ch)
                count = 1
            if ch not in seen:
                seen.add(ch)
                count += 1
            if count > mc:
                    mc = count
        return mc