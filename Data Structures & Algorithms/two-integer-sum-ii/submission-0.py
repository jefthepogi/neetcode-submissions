class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        size = len(numbers) - 1
        R = size
        L = 0
        while True:
            Rval = numbers[R]
            Lval = numbers[L]
            total = Lval + Rval
            if total == target:
                break
            if L == R:
                continue

            if total > target:
                R -= 1
            elif total < target:
                L += 1
            

                
        
        return [L + 1, R + 1]