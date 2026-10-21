class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        last_row = "01"
        i = 2
        while i < n:
            ref = last_row
            len_ = len(ref)
            j = 0
            out = ""
            while j < len_:
                if ref[j] == "0":
                    out += "01"
                else:
                    out += "10"
                j += 1
            last_row = out
            i += 1
        return int(last_row[k - 1])
