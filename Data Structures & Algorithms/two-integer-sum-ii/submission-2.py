class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        R = len(numbers) - 1
        L = 0
        while True:
            total = numbers[R] + numbers[L]
            if total == target:
                break

            if total > target:
                R -= 1
            elif total < target:
                L += 1    
        
        return [L + 1, R + 1]