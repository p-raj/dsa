class Solution:
    def trap(self, height: List[int]) -> int:
        H = height
        res = 0
        lft = 0
        rgt = len(H) - 1

        lft_max = H[0]
        rgt_max = H[-1]

        while lft < rgt:
            lft_max = max(lft_max, H[lft])
            rgt_max = max(rgt_max, H[rgt])

            if lft_max <= rgt_max:
                res += (lft_max - H[lft])
                lft += 1
            else:
                res += (rgt_max - H[rgt])
                rgt -= 1
        return res