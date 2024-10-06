class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        temp = [0] * (len(matrix[0]) + 1)
        result = 0

        for row in matrix:
            for idx, el in enumerate(row):
                if el == "1":
                    temp[idx] += 1
                else:
                    temp[idx] = 0

            stack = []
            for i in range(len(temp)):
                while stack and temp[i] < temp[stack[-1]]:
                    temp_id = stack.pop()
                    height = temp[temp_id]
                    width = i - (stack[-1] + 1) if stack else i
                    result = max(result, width * height)
                stack.append(i)

        return result
