class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        answer = maximum = 0
        previous = None
        for color, time in zip(colors, neededTime):
            if color != previous: maximum = 0
            answer += min(maximum, time)
            maximum = max(maximum, time)
            previous = color
        return answer
