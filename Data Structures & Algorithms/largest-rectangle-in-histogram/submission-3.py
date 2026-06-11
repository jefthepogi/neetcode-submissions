class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        size = len(heights)
        for R in range(size + 1):
            h = heights[R] if R < size else 0
            L = R
            while stack and stack[-1][1] > h:
                L, h_i = stack.pop()
                maxArea = max(maxArea, (R - L)*h_i)
            stack.append((L, h))
        return maxArea