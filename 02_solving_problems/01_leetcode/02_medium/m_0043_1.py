class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        result = 0
        str_res = ""
        carry1 = 1
        
        for c1 in num1[::-1]:
            n1 = ord(c1) - 48
            carry2 = 1
            for c2 in num2[::-1]:
                n2 = ord(c2) - 48
                result += carry1 * carry2 * n1 * n2
                carry2 *= 10
            carry1 *= 10

        while result:
            c = chr(48 + (result % 10))
            result //= 10
            str_res = c + str_res

        return str_res


# OK, 46%, 28%