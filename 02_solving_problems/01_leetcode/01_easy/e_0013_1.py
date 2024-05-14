class Solution:
    def romanToInt(self, s: str) -> int:
        convert_dct = { "MMM": 3000, "MM": 2000, "M": 1000, 
                        "CM": 900, "D": 500,
                        "CD": 400, "CCC": 300, "CC": 200, "C": 100,
                        "XC": 90, "L": 50,
                        "XL": 40, "XXX": 30, "XX": 20, "X": 10,
                        "IX": 9, "V": 5,
                        "IV": 4, "III": 3, "II": 2, "I": 1 }
        result = 0

        left_mono = right = len(s) - 1
        
        while right >= 0:
            if left_mono - 1 >= 0 and convert_dct[s[left_mono - 1]] <= convert_dct[s[left_mono]]:
                left_mono -= 1
            else: 
                result += convert_dct[s[left_mono:right + 1]]
                left_mono -= 1
                right = left_mono

        return result

        #OK, 82%, 18%