class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = [c for c in s]
        stack = []
        v = [True] * len(s)
        for idx, c in enumerate(s):
            if not stack and c == ")":
                v[idx] = False
            elif stack and c == ")":
                stack.pop()
            elif c == "(":
                stack.append(idx)
        for idx in stack:
            v[idx] = False

        return "".join([c for c,i in zip(s,v) if i])