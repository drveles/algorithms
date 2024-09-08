class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c not in "()":
                continue
            if c == "(":
                stack.append(c)
            elif c == ")" and stack and stack[-1] == "(":
                stack.pop()
            else: return False

        return not stack

    def removeInvalidParentheses(self, s: str) -> List[str]:
        if self.isValid(s):
            return [s]

        n = len(s)
        result = [{s, }]
        flag = False

        while n and not flag:
            curr_results = set()
            for temp_s in result[-1]:
                for idx in range(len(temp_s)):
                    curr_results.add(temp_s[:idx] + temp_s[idx + 1 :])
            result.append(curr_results)

            for curr_res in curr_results:
                if self.isValid(curr_res):
                    flag = True

        return [el for el in result[-1] if self.isValid(el)]


# OK, 47%, 15%
