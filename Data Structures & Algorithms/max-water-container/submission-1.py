class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lft, rgt = 0, len(heights)-1
        max_area = -1
        while lft < rgt:
            area = min(heights[lft], heights[rgt]) * (rgt-lft)
            if area > max_area:
                max_area = area
            if heights[lft] <= heights[rgt]:
                lft += 1
            else:
                rgt -= 1
        return max_area