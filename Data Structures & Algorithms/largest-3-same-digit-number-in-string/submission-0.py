class Solution:
    def largestGoodInteger(self, num: str) -> str:
        gn = ""
        i = 0
        while i < len(num) - 2:
            if num[i] == num[i + 1] == num[i + 2]:
                if (gn and gn[0] < num[i]) or len(gn) == 0:
                    gn = num[i] + num[i + 1] + num[i + 2]
                i += 2
            i += 1
        return gn
