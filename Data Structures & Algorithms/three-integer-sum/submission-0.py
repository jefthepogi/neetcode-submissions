class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        size = len(nums) - 1
        res = set()
        numbers = sorted(nums)

        for i, n in enumerate(numbers):
            L = i + 1
            R = size
            target = -n

            while L < R:

                lval = numbers[L]
                rval = numbers[R]
                total = lval + rval

                if total == target:
                    res.add(tuple([lval, rval, n]))
                    L += 1
                    R -= 1

                elif total > target:
                    R -= 1
                elif total < target:
                    L += 1

        return [list(x) for x in res]