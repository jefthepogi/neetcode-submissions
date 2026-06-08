class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {'(': ')', '[': ']', '{' : '}'}
        for c in s:
            if c in (')', '}', ']'):
                if len(stack) == 0:
                    return False
                if stack[-1] != c:
                    return False
                stack.pop()
                continue

            stack.append(pair[c])
        
        return len(stack) == 0