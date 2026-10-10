class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cur = None
        prv = None
        nxt = None
        F = flowerbed
        i = 0
        while i < len(F) and n > -1:
            cur = F[i]
            prv = None if i == 0 else F[i - 1]
            nxt = None if i == (len(F) - 1) else F[i + 1]
            if not prv and not nxt and not cur:
                F[i] = 1
                n -= 1
            i += 1
        return n <= 0
