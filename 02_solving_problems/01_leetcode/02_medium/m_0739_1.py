class Solution:
    def dailyTemperatures(self, temperatures):
        mono_stack = []

        result = [0 for _ in range(len(temperatures))]

        for id, el in enumerate(temperatures):
            if not mono_stack:
                mono_stack.append(id)
                continue
            while mono_stack and temperatures[mono_stack[-1]] < el:
                result[mono_stack[-1]] = id - mono_stack[-1]
                mono_stack.pop()
            else:
                mono_stack.append(id)

        return result
