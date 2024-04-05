class Solution:
    def convert(self, s: str, numRows: int) -> str:
        len_s = len(s)
        if numRows == 1 or numRows >= len_s:
            return s
        count_steps = 0
        answer = ''


        while count_steps < numRows:
            for i in range(count_steps, len_s, numRows + numRows - 2):
                answer += s[i]
                if 0 < count_steps < numRows - 1:
                    dept = numRows - (count_steps + 1)
                    if i + (dept * 2) < len_s:
                        answer += s[i + (dept * 2)]
            count_steps += 1
        
        return answer

# OK 52% time, 75% mem