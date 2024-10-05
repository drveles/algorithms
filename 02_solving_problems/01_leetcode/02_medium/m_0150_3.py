class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []

        for token in tokens:
            if token == "+":
                temp = operands.pop()
                operands[-1] += temp
            elif token == "-":
                temp = operands.pop()
                operands[-1] -= temp
            elif token == "/":
                temp = operands.pop()
                operands[-1] = int(operands[-1] / temp)
            elif token == "*":
                temp = operands.pop()
                operands[-1] *= temp
            else:
                operands.append(int(token))
        
        return operands[-1]
