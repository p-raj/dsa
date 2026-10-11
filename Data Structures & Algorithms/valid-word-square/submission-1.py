class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        rows = len(words)
        cur_r = 0
        while cur_r < rows:
            cur_c = cur_r
            r = 0
            row_str = words[cur_r]
            col_str = ""
            while r < rows and r < len(row_str):
                col_str += words[r][cur_c]
                r += 1
            if row_str != col_str:
                return False
            cur_r += 1
        return True