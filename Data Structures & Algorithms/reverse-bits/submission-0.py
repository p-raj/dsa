class Solution:
    def reverseBits(self, n: int) -> int:
        x = 0
        for i in range(32):
            bit = (n >> (31 - i)) & 1
            x |= bit << i
        return x