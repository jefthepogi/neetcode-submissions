class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        arr = sorted(nums)
        base = arr[0]
        lens = []
        currlen = 1
        for n in arr[1:]:
            if base != n - 1:
                if base == n:
                    continue
                lens.append(currlen)
                currlen = 0
            currlen += 1
            base = n
        lens.append(currlen)
        return max(lens)
