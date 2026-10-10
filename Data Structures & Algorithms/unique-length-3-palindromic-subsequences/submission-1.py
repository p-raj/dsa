class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        len_ = len(s)
        prefix = [[0] * 26 for _ in range(len_ + 1)]
        # prefix[chr][idx]
        # count of char in s[0:i-1]
        lft_index = [-1] * 26
        rgt_index = [-1] * 26

        for idx, char in enumerate(s):
            cidx = ord(char) - ord("a")
            if lft_index[cidx] == -1:
                lft_index[cidx] = idx
            rgt_index[cidx] = idx
            # copy the last state
            prefix[idx + 1] = prefix[idx][:]
            # incr the char count
            prefix[idx + 1][cidx] += 1

        res = 0
        # for all the chars
        # check if they form start and end
        for idx in range(26):
            if lft_index[idx] == -1 or lft_index[idx] == rgt_index[idx]:
                continue
            # we need to check for middle elements
            # between lft_index[idx] and rgt_index[idx]
            for mid in range(26):
                if prefix[rgt_index[idx]][mid] - prefix[lft_index[idx]+1][mid] > 0:
                    res += 1

        return res