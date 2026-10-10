class Solution:
    def bins(self, arr, lft, rgt, target):
        if lft > rgt:
            return lft
        mid = (lft + rgt)//2
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            return self.bins(arr, lft, mid-1, target)
        else:
            return self.bins(arr, mid+1, rgt, target)

    def get_col_arr(self, matrix, col):
        return [matrix[r][col] for r in range(len(matrix))]

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        visited_r = set()
        scan_r = 0
        while True:
            if scan_r in visited_r:
                return False
            visited_r.add(scan_r)
            scan_c = self.bins(matrix[scan_r], 0, cols-1, target)
            scan_c = cols-1 if scan_c >= cols else scan_c
            scan_c = 0 if scan_c < 0 else scan_c

            col_arr = self.get_col_arr(matrix, scan_c)
            scan_r = self.bins(col_arr, 0, len(col_arr)-1, target)
            scan_r = rows-1 if scan_r >= rows else scan_r
            scan_r = 0 if scan_r < 0 else scan_r

            if matrix[scan_r][scan_c] == target:
                return True
        return False
