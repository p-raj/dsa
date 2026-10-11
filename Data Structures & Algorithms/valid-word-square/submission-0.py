class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        rows = len(words)
        r = 0
        while r < len(words):
            row_str = words[r]
            c = r
            col_str = ""
            while c < len(words):
                col_str += words[r][c]
                c += 1
            if row_str == col_str:
                return True
            r += 1
        return False