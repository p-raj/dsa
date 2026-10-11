class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        R = {}
        C = {}
        P = picture
        rows, cols = len(P), len(P[0])
        r, c = 0, 0
        while r < rows:
            if r not in R:
                R[r] = set()
            c = 0
            while c < cols:
                if c not in C:
                    C[c] = set()
                if P[r][c] == 'B':
                    R[r].add(c)
                    C[c].add(r)
                c += 1
            r += 1
        r, c = 0, 0
        lonely = 0
        while r < rows:
            c = 0
            while c < cols:
                if P[r][c] == 'B':
                    if len(R[r]) <= 1 or len(C[c]) <= 1:
                        lonely += 1
                c += 1
            r += 1
        return lonely