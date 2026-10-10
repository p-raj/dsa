class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        up, dn = 0, 1
        common = set()
        while up < rows - 1:
            dn = up + 1
            com = set(mat[up]).intersection(set(mat[dn]))
            if not com:
                return -1
            if common:
                common = common.intersection(com)
                if not common:
                    return -1
            else:
                common = com
            up += 1
        
        common = list(common)
        common.sort()
        return common[0]