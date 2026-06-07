class Solution:
    def trap(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
        left, right = height[L], height[R]
        water = 0
        while L < R:
            if height[L] < height[R]:
                L += 1
                left = max(left, height[L])
                water += left - height[L]
            else:
                R -= 1
                right = max(right, height[R])
                water += right - height[R]

        return water
