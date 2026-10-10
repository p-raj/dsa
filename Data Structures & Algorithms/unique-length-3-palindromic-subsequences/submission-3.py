class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        len_ = len(s)
        lft_idx = [-1] * 26
        rgt_idx = [-1] * 26

        # track left and right
        for idx, char in enumerate(s):
            cidx = ord(char) - ord("a")
            if lft_idx[cidx] == -1:
                lft_idx[cidx] = idx
            rgt_idx[cidx] = idx

        count = 0

        for i in range(26):
            if lft_idx[i] == -1 or rgt_idx[i] == lft_idx[i]:
                continue
            mask = 0
            lft, rgt = lft_idx[i] + 1, rgt_idx[i]
            # for all the elements that lie bettween
            # the lft and right
            for i in range(lft, rgt):
                c = ord(s[i]) - ord('a')
                # already counted
                if mask & (1 << c):
                    continue
                # count and add to mask
                mask |= (1 << c)
                count += 1

        return count
