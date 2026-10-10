class Stack:
    def __init__(self):
        self.s = []

    def push(self, v):
        self.s.append(v)

    def pop(self):
        return self.s.pop()

    def is_empty(self):
        return len(self.s) == 0

    def peek(self):
        if not self.is_empty():
            return self.s[len(self.s) - 1]


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t = temperatures
        res = [0] * len(t)
        stack = Stack()
        lft = 0
        for idx, temp in enumerate(t):
            while not stack.is_empty() and temp > stack.peek()[1]:
                i, v = stack.pop()
                res[i] = idx - i
            stack.push((idx, temp))
        return res


