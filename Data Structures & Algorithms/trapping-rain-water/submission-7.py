class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        rgt = 0
        H = height
        while rgt < len(H):
            while stack and H[stack[-1]] < H[rgt]:
                pin = stack.pop()
                if not stack:
                    break
                lft = stack[-1]
                wdt = rgt - lft - 1
                hgt = min(H[lft], H[rgt]) - H[pin]
                res += hgt * wdt
            stack.append(rgt)
            rgt += 1
        return res