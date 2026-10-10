class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        H = heights
        S = sorted(H)
        for idx in range(len(H)):
            if S[idx] != H[idx]:
                count += 1
        return count