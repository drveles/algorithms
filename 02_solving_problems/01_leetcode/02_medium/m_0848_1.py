class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        result = ''
        temp_summ = 0

        def shift(char:str, shift_num) -> str:
            num = (ord(char) - ord('a') + shift_num) % 26
            return chr(num + ord('a'))

        for idx in range(len(s) - 1, -1, -1):
            temp_summ = temp_summ + shifts[idx]
            result += shift(s[idx], temp_summ)

        return result[::-1]
