

class Solution():
    class MaxStack():
        @staticmethod
        def decorator(func):
            def wrapper(*args, **kwargs):
                print(func(*args, **kwargs))
                return func
            return wrapper

        def __init__(self):
            self.stack = []
            self.max_arr = []
        
        def push(self, el):
            self.stack.append(el)

            if not self.max_arr:
                self.max_arr.append(el)
            else:
                self.max_arr.append(max(el, self.max_arr[-1]))
        
        @decorator
        def pop(self):
            if self.stack:
                self.max_arr.pop()
                return self.stack.pop()
        
        # @decorator
        def get_max(self):
            if self.max_arr:
                return self.max_arr[-1]
        
if __name__ == "__main__":
    maxic = Solution().MaxStack()
    print()
    maxic.push(7)
    maxic.push(8)
    maxic.push(8)

    maxic.push(9)

    maxic.get_max()
    maxic.pop()
    maxic.get_max()
    maxic.pop()
    maxic.get_max()
    maxic.pop()
    maxic.get_max()
    maxic.pop()