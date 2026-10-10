class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        len_ = len(s)
        shft = 0
        for d, mov in shift:
            if d:
                shft += mov
            else:
                shft -= mov
        shft = shft % len_
        return s[len_-shft:] + s[:len_-shft]