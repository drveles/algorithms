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

    def getMin(self) -> int:
        if self.items:
            return min(self.items)
        else:
            return 0


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# normal solution, but slow
# 5% time, 99% mem