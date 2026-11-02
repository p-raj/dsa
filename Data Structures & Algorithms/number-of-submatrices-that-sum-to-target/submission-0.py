class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:

        def countArrSumTarget(arr: List[int], target: int) -> int:
            count = 0
            pfx = {0: 1}
            tot = 0
            for num in arr:
                tot += num
                count += pfx.get(tot - target, 0)
                pfx[tot] = pfx.get(tot, 0) + 1
            return count

        rows = len(matrix)
        cols = len(matrix[0])

        res = 0
        for top in range(rows):
            sumM = [0 for c in range(cols)]
            for bottom in range(top, rows):
                for idx, num in enumerate(matrix[bottom]):
                    sumM[idx] += num
                res += countArrSumTarget(sumM, target)
        return res
        # crows = 0
        # # n2
        # for row in matrix:
        #     crows += countArrSumTarget(row, target)

        # ccols = 0
        # # n2
        # for col in range(cols):
        #     crr = []
        #     for row in range(len(matrix)):
        #         crr.append(matrix[row][col])
        #     ccols += countArrSumTarget(crr, target)

        # sumM = [matrix[0][c] for c in range(cols)]
        # cmats = 0
        # for ridx, row in enumerate(matrix):
        #     if ridx == 0:
        #         continue
        #     for idx, num in enumerate(row):
        #         sumM[idx] += row[idx]
        #     print(sumM)
        #     cmats += countArrSumTarget(sumM, target)


        return ccols + crows + cmats
