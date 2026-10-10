class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_a = -1
        for idx, h in enumerate(heights):
            if not stack:
                stack.append((idx, h))
            else:
                pi, _ = idx, h
                while stack and stack[-1][1] >= h:
                    pi, ph = stack.pop()
                    ar = (idx - pi) * ph
                    if ar > max_a:
                        max_a = ar
                stack.append((pi, h))
        # pi, ph = stack.pop()
        while stack:
            pi, ph = stack.pop()
            ar = (len(heights) - pi) * ph
            if ar > max_a:
                max_a = ar
        return max_a
