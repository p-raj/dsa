class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for d, m in shift:
            i = 0
            if d:
                # ->
                while i < m:
                    i += 1
                    s = s[-1] + s[:-1]
            else:
                # <-
                while i < m:
                    i += 1
                    s = s[1:] + s[0]
        return s