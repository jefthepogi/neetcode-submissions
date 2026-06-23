class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        targetRow = None

        for i, n in enumerate(matrix):
            if n[0] <= target and n[-1] >= target:
                targetRow = i
                break
        
        if targetRow is None:
            return False

        L = 0
        R = len(matrix[targetRow]) - 1

        while L <= R:
            m = (L + R) // 2
            current = matrix[targetRow][m]
            if target == current:
                return True

            if current > target:
                R = m - 1
            elif current < target:
                L = m + 1

        return False