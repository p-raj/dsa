class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        cur = 0
        while True:
            if cur >= len(strs[0]):
                return lcp
            to_match = strs[0][cur]
            match = True
            for s in strs:
                if cur >= len(s):
                    return lcp
                match = match and (s[cur] == to_match)
                if not match:
                    return lcp
            lcp += to_match
            cur += 1
        return lcp
