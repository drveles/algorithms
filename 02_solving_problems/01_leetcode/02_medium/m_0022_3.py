class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def dfs(ctr_left, ctr_right, string):
            if ctr_left == ctr_right and ctr_left + ctr_right == n * 2:
                result.append(string)

            if ctr_left < n:
                dfs(ctr_left + 1, ctr_right, string + "(")

            if ctr_right < ctr_left:
                dfs(ctr_left, ctr_right + 1, string + ")")

        dfs(0, 0, "")
        return result
