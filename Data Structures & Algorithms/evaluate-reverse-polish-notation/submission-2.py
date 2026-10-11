import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 3:
            print(f"{tokens[0]} {tokens[2]} {tokens[1]}")
            v = (eval(f"{tokens[0]}{tokens[2]}{tokens[1]}"))
            if v > 0:
                return math.floor(v)
            else:
                return math.ceil(v)
        stack = []
        for t in tokens:
            if t in {"+", "-", "*", "/"}:
                suf = stack.pop()
                pri = stack.pop()
                v = self.evalRPN([pri, suf, t])
                stack.append(v)
            else:
                stack.append(t)
            print(stack)
        return stack[-1]
