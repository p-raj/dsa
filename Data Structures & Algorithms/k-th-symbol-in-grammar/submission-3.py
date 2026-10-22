class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        cur = 0
        lft, rgt = 1, 2 ** (n - 1)
        for _ in range(n - 1):
            mid = (lft + rgt) // 2
            if k <= mid:
                rgt = mid
            else:
                lft = mid + 1
                cur = 0 if cur else 1
        return cur
