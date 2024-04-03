class Solution:
    class Stack:
        def __init__(self):
            self.items = []

        def pop(self):
            if self.items:
                return self.items.pop()
            else:
                return 0

        def push(self, item):
            self.items.append(item)

    def isValid(self, s: str) -> bool:
        res_flag = True
        stack = self.Stack()
        for c in s:
            if c in "([{":
                stack.push(c)
            elif c == ")" and stack.pop() == "(":
                continue
            elif c == "]" and stack.pop() == "[":
                continue
            elif c == "}" and stack.pop() == "{":
                continue
            else:
                res_flag = False
                break

        if stack.pop():
            res_flag = False

        return res_flag


# normal solution using stack.
# 20% runtime, 75% mem