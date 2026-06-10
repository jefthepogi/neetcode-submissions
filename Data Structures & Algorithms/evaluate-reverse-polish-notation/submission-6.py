class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in ('+', '-', '*', '/'):
                if t == '+':
                    stack.append(stack.pop() + stack.pop())
                elif t == '-':
                    minuend = stack.pop()
                    stack.append(stack.pop() - minuend)
                elif t == '*':
                    stack.append(stack.pop() * stack.pop())
                else:
                    dividend = stack.pop()
                    stack.append(int(stack.pop() / dividend))
                continue
            stack.append(int(t))

        return stack[-1]