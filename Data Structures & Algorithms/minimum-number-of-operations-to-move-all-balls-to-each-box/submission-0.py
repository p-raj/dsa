class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        len_ = len(boxes)
        if len_ < 2:
            return 0
        P = [0] * len_
        for i in range(len_):
            for j in range(i + 1, len_):
                if boxes[j] == "1":
                    P[i] += j - i
        S = [0] * len_
        i = len_ - 1
        while i > -1:
            j = i - 1
            while j > -1:
                if boxes[j] == "1":
                    S[i] += i - j
                j -= 1
            i -= 1
        return [p+s for p,s in zip(P,S)]
