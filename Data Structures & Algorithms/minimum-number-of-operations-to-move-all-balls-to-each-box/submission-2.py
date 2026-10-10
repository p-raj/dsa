class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        len_ = len(boxes)
        if len_ < 2:
            return [0]
        res = [0] * len_

        balls = 0
        moves = 0
        for i in range(len_):
            res[i] = balls + moves
            moves += balls
            balls += 1 if boxes[i] == "1" else 0

        balls = 0
        moves = 0
        for i in range(len_ - 1, -1, -1):
            res[i] += balls + moves
            moves += balls
            balls += 1 if boxes[i] == "1" else 0

        return res
