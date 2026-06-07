class Solution:
    def maxArea(self, heights: List[int]) -> int:
        R = len(heights) - 1
        L = 0
        lastarea = (R-L) * min(heights[L], heights[R])
        while L < R:
            left = heights[L]
            right = heights[R]

            area = (R-L) * min(left, right)
            if area > lastarea:
                lastarea = area

            if left < right:
                L += 1
            else: R -= 1

        return lastarea
