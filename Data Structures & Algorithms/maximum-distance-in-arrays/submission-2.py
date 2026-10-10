class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        gmin, gmax = arrays[0][0], arrays[0][-1]
        maxd = 0
        for i in range(1, len(arrays)):
            curr = arrays[i]
            maxd = max(
                maxd,
                abs(
                    curr[0]-gmax
                ),
                abs(
                    curr[-1]-gmin
                )
            )
            gmin = min(gmin, curr[0])
            gmax = max(gmax, curr[-1])
        return maxd