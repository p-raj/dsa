class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # X = [0,1...xn]
        # Odd sum = odd + even, even + odd
        # Ei, Oi are Evens and Odds at i
        # new even -> previous sum (e -> e), (o -> o)
        # new odd -> previous sum (e -> o), (o -> e)
        # (O,E) = (0,0)
        # 0 -> 0 (0,1), 00 -> 0 (0,2), 000 -> 0 (0,3) -> 0001 -> 4 (1,3)
        # 1 -> 1 (1,0), 11 -> 2 (2,0), 111 -> 4 (3,0) -> 1111 -> 6 (4,0)
        # 1 -> 1 (1,0), 11 -> 2 (2,0), 110 -> 3 (2,1) -> 1100 -> 4 (2,2)
        # 1 -> 1 (1,0), 10 -> 2 (1,1), 101 -> 4 (2,1) -> 1010 -> 6 (2,2)
        # 0 -> 0 (0,1), 01 -> 2 (1,1), 010 -> 3 (1,2) -> 0101 -> 6 (2,2)
        # including the new element -
        # O: count(arr) making  odd-sum on odd -> even
        # O: count(arr) making even-sum on odd -> odd
        # E: count(arr) making  odd-sum on odd -> odd
        # E: count(arr) making even-sum on even -> even
        arr_e = 0
        arr_o = 0
        res = 0
        for num in arr:
            # odd
            if num % 2:
                arr_o, arr_e = arr_e+1, arr_e
            # even
            else:
                arr_e += 1
            res += arr_o
        return res