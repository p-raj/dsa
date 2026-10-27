class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:

        def expand(enc: List[List[int]]) -> List[int]:
            res = []
            for num, rep in enc:
                res.extend([num] * rep)
            return res

        def compress(dec: List[int]) -> List[List[int]]:
            res = []
            lft = 0
            while lft < len(dec):
                rgt = lft
                count = 0
                while rgt < len(dec) and dec[lft] == dec[rgt]:
                    count += 1
                    rgt += 1
                res.append([dec[lft], count])
                lft = rgt
            return res

        return compress([l * r for l, r in zip(expand(encoded1), expand(encoded2))])
