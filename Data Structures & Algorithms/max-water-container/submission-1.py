class Solution:
    def maxArea(self, heights: List[int]) -> int:
        R = len(heights) - 1
        L = 0
        area = 0
        while L < R:
            left = heights[L]
            right = heights[R]

            area = max(area, (R-L) * min(left, right))

            if left < right:
                L += 1
            else: R -= 1

        return area
