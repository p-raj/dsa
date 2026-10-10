class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        ti = 0

        for ch in s:
            if ti < len(t) and ch == t[ti]:
                ti += 1

        return len(t) - ti