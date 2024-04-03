class Solution:
    class MinStack:
        def __init__(self):
            self.items = []

        def push(self, val: int) -> None:
            self.items.append(val)

        def pop(self) -> None:
            if self.items:
                return self.items.pop()

        def top(self) -> int:
            if self.items:
                return self.items[-1]

    def evalRPN(self, tokens: List[str]) -> int:
        nums_stack = self.MinStack()
        operators_set = {"+", "-", "*", "/"}

        for el in tokens:
            if el in operators_set:
                y, x = nums_stack.pop(), nums_stack.pop()
                if el == "-":
                    nums_stack.push(x - y)
                elif el == "+":
                    nums_stack.push(x + y)
                elif el == "*":
                    nums_stack.push(x * y)
                elif el == "/":
                    nums_stack.push(int(x / y))
            else:
                nums_stack.push(int(el))

        return nums_stack.pop()


# good solution,
# runtime 61%, mem 84%
