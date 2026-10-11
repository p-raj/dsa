class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # [0:10][10:11][11:13][13:]
        count = 0
        for item in details:
            if item[11] in ('6','7','8','9'):
                count += 1
        return count