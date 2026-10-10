class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        if rowIndex == 0:
            return row
        idx = 0
        while idx < rowIndex:
            pr = [0] + row + [0]
            i = 0
            r = []
            while i < len(pr) - 1:
                r.append(pr[i] + pr[i+1])
                i += 1
            row = r
            idx += 1
        return row