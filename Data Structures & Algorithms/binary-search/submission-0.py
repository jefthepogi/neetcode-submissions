class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1

        while L <= R:
            mid = (L + R) // 2
            curr = nums[mid]

            if curr == target:
                return mid

            if curr > target:
                R = mid - 1
            else:
                L = mid + 1

        return -1