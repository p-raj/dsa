class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        rows = ["0", "01"]
        i = 2
        while i < n:
            ref = rows[i - 1]
            len_ = len(ref)
            j = 0
            out = ""
            while j < len_:
                if ref[j] == "0":
                    out += "01"
                else:
                    out += "10"
                j += 1
            rows.append(out)
            i += 1
        return int(rows[n - 1][k - 1])
