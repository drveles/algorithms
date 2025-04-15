class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        n = len(questions)
        temp_arr = [0] * n
        temp_arr[-1] = questions[-1][0]

        idx = n - 2
        while idx >= 0:
            points, brainpower = questions[idx]
            temp_idx = idx + brainpower + 1
            if temp_idx < n:
                temp_arr[idx] = max(points, points + temp_arr[temp_idx], temp_arr[idx+1])
            else: 
                temp_arr[idx] = max(points, temp_arr[idx+1])
            idx -= 1

        return temp_arr[0]
