class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # log(mn) = log(m) + log(n)
        # bin(row) + bin(col)
        # which col -> search in row
        # collect elems of that col
        # run bin search
        def bins(arr, lft, rgt):
            if lft > rgt:
                return lft
            mid = (lft + rgt)//2
            if arr[mid] >= target:
                return bins(arr, lft, mid-1)
            else:
                return bins(arr, mid+1, rgt)

        c = bins(matrix[0], 0, len(matrix[0])-1)
        if c == len(matrix[0]):
            c = len(matrix[0]) - 1
        elif c < 0:
            c = 0
        colarr = [matrix[row][c] for row in range(len(matrix))]
        r = bins(colarr, 0, len(colarr)-1)
        if r == len(matrix) or r < 0:
            return False
        return target == matrix[r][c]