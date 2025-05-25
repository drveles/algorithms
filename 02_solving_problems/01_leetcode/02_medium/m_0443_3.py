class Solution:
    def compress(self, chars: List[str]) -> int:
        left = right = 0 

        while right < len(chars):
            char = chars[right]
            ctr = 0
            while right < len(chars) and chars[right] == char:
                right += 1
                ctr += 1
            chars[left] = char
            for symb in str(ctr) if ctr > 1 else '':
                left += 1
                chars[left] = symb
            left += 1

        return left
