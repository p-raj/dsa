class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in {"{", "(", "["}:
                stack.append(s[i])
            else:
                if (
                    (stack[-1] == "{" and s[i] == "}")
                    or (stack[-1] == "(" and s[i] == ")")
                    or (stack[-1] == "[" and s[i] == "]")
                ):
                    stack.pop()
        print(stack)
        return False if stack else True
