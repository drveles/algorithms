class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if token.lstrip('-').isdigit():
                stack.append(int(token))
            elif token == '-':
                y, x = stack.pop(), stack.pop()
                stack.append(x - y)
            elif token == '+':
                y, x = stack.pop(), stack.pop()
                stack.append(x + y)
            elif token == '*':
                y, x = stack.pop(), stack.pop()
                stack.append(x * y)
            elif token == '/':
                y, x = stack.pop(), stack.pop()
                stack.append((int(x / y)))

        return stack[0]


#OK, 70%, 65%