class Solution:
    def intToRoman(self, num: int) -> str:
        roman_dct = {3000: "MMM", 2000: "MM", 1000: 'M',
                     900: "CM", 800: "DCCC", 700: "DCC", 600: "DC",
                     500: "D", 400: "CD", 300: "CCC", 200: "CC", 100: "C",
                     90: "XC", 80: "LXXX", 70: "LXX", 60: "LX", 50: "L",
                     40: "XL", 30: "XXX", 20: "XX", 10: "X",
                     9: "IX",  8: "VIII", 7: "VII", 6: "VI", 5: "V",
                     4: "IV", 3: "III", 2: "II", 1: "I" }
        res = ""

        if num > 999: 
            temp = (num // 1000) * 1000
            num = num % 1000
            res += roman_dct.get(temp, '')

        if num > 99: 
            temp = (num // 100) * 100
            num = num % 100
            res += roman_dct.get(temp, '')

        if num > 9: 
            temp = (num // 10) * 10
            num = num % 10
            res += roman_dct.get(temp, '')
        
        res += roman_dct.get(num, '')

        return res


#OK 30%, 7%