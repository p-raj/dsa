import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 3:
            return math.floor(eval(f"{tokens[1]}{tokens[2]}{tokens[0]}"))
        stack = []
        for t in tokens:
            if t in {"+", "-", "*", "/"}:
                v1 = stack.pop()
                v2 = stack.pop()
                v3 = self.evalRPN([v1, v2, t])
                stack.append(v3)
            else:
                stack.append(t)
        return stack[-1]