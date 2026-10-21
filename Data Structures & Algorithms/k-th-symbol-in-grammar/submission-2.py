class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        val = k - 1
        par = 0
        while val > 0:
            par ^= val & 1
            val >>= 1
        return par