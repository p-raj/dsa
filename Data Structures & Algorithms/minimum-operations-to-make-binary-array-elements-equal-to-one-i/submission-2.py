class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = nums
        len_ = len(N)
        lft = 0
        count = 0
        while lft < (len_ - 2):
            rgt = lft
            while rgt < len_ and N[rgt]:
                rgt += 1
            if rgt == len_:
                return count
            lft = rgt
            jump = 0
            if lft < (len_ - 2):
                if N[lft] == 0:
                    jump = 1
                    N[lft] = 1
                    if N[lft + 1] == 0:
                        jump = 2
                        N[lft + 1] = 1
                        if N[lft + 2] == 0:
                            jump = 3
                            N[lft + 2] = 1
                        else:
                            N[lft + 2] = 0
                            jump = 2
                    else:
                        N[lft + 1] = 0
                        jump = 1
                else:
                    N[lft + 1] = 1
                    jump = 0
                count += 1
                lft += jump
            if lft == (len_ - 2) and N[lft] == N[lft + 1] == N[lft + 1] == 0:
                count += 1
            elif lft == (len_ - 2) and not (N[lft] == N[lft + 1] == N[lft + 1] == 1):
                return -1
        return count
