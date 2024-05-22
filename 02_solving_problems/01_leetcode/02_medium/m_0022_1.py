class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left, right, temp_str):
            if len(temp_str) == n * 2:
                result.append(temp_str)
                return
            
            if left < n:
                dfs(left + 1, right, temp_str + "(")

            if right < left:
                dfs(left, right + 1, temp_str + ')')
        
        result = []
        dfs(0, 0, '')

        return result

# OK, 32%, 89%