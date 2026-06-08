class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in (')', '}', ']'):
                if len(stack) == 0:
                    return False
                if stack[-1] != c:
                    return False
                stack.pop()
                continue
                
            match c:
                case '(':
                    stack.append(')')
                case '{':
                    stack.append('}')
                case '[':
                    stack.append(']')
        
        return len(stack) == 0