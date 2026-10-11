class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 3:
            return eval(f"{tokens[0]}{tokens[2]}{tokens[1]}")
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