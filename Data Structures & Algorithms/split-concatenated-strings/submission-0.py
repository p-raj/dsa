class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        for idx, s in enumerate(strs):
            strs[idx] = max(s, s[::-1])
        strs = sorted(strs, reverse=True)
        return "".join(strs)
