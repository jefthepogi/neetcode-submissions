class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        size = len(heights)
        boundaries = [1] * size
        stack = []
        for i in range(size):
            c = i - 1
            while c >= 0:
                if heights[c] < heights[i]:
                    break
                c -= 1
                boundaries[i] += 1

        for i in range(size - 1, -1, -1):
            c = i + 1
            while c < size:
                if heights[c] < heights[i]:
                    break
                c += 1
                boundaries[i] += 1
        
        for i, h in enumerate(heights):
            highest = h * (boundaries[i])
            if not stack:
                stack.append(highest)
                continue

            if highest > stack[-1]:
                stack.append(highest)

        return stack[-1]