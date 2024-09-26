class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left = right = 0
        result = []
        queue = [(left,right,"",)]

        while queue:
            left, right, string = queue.pop()
            if len(string) == n * 2:
                result.append(string)
            if left < n:
                queue.append((left + 1, right, string + "("))
            if right < left: 
                queue.append((left, right + 1, string + ")"))
        
        return result

