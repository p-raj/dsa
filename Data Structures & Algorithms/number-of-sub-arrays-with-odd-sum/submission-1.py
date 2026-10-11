import math
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        E = list(filter(lambda x: x%2 == 0, arr))
        O = list(filter(lambda x: x%2 == 1, arr))
        if not O:
            return 0
        print(E)
        print(O)
        print(len(E))
        print(len(O))
        # # Total items (n) and choosing (k)
        # n = 7
        # k = 5

        # # Get the total count of combinations
        # total_combinations = math.comb(n, k)
        # print(total_combinations)  # Output: 21
        sm = 0
        leno_ = len(O)
        lene_ = len(E)
        for i in range(1, leno_+1, 2):
            sm += math.comb(leno_, i)
        if not lene_:
            return sm
        for i in range(0, lene_+1):
            sm += math.comb(lene_, i)

        return sm
        