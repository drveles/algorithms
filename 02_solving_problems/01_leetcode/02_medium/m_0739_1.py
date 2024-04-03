class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mono_stack = []
        t_len = len(temperatures)
        result = [0 for _ in range(t_len)]
        
        for id in range(t_len):
            if not mono_stack:
                mono_stack.append(id)
                continue
            while mono_stack and temperatures[mono_stack[-1]] < temperatures[id]: 
                result[mono_stack[-1]] = id - mono_stack[-1]
                mono_stack.pop()
            else:
                mono_stack.append(id)

        return result


# normal solution, using monotonic stack
# 39% time, 59% mem