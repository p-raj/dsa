class Solution:
    def scoreOfString(self, s: str) -> int:
        sum_ = 0
        i = 0
        for i in range(0, len(s)-1, 1):
            # print(i, s[i+1], ord(s[i+1]), s[i], ord(s[i]))
            sum_ += abs(ord(s[i+1])-ord(s[i]))
        return sum_