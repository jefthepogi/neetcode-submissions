class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, val in enumerate(temperatures):
            while stack:
                if temperatures[stack[-1]] < val:
                    temp_index = stack.pop()
                    res[temp_index] = i - temp_index
                    continue
                break

            stack.append(i)            
        
        return res

