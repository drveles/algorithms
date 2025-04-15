class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        n = len(questions)
        temp_arr = [0] * (n + 1)

        idx = n - 1
        while idx >= 0:
            points, brainpower = questions[idx]
            temp_idx = idx + brainpower + 1
            points_after_step = temp_arr[temp_idx] if temp_idx < n else 0
            temp_arr[idx] = max(temp_arr[idx+1], points + points_after_step)
            idx -= 1

        return temp_arr[0]
