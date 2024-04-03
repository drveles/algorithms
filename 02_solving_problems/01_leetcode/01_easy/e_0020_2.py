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
        open_set = {"(", "[", "{"}

        for c in s:
            if c in open_set:
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


# good solution -  search in set much better than search in str
# 67% runtime, 75% mem
