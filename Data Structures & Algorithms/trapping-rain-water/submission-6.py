class Solution:
    def trap(self, height: List[int]) -> int:
        # using monotonic stack
        stack = []
        H = height
        rgt = 0
        res = 0
        for rgt in range(len(H)):
            while stack and H[stack[-1]] < H[rgt]:
                pin = stack.pop()
                if not stack:
                    break
                lft = stack[-1]
                width = rgt - lft - 1
                depth = min(H[lft], H[rgt]) - H[pin]
                res += (depth * width)
            stack.append(rgt)

        return res