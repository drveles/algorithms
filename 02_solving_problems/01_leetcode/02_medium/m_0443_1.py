class Solution:
    def compress(self, chars: List[str]) -> int:
        left = right = 0
        left_char = chars[left]

        def _compress(left: int, right: int) -> int:
            str_num = list(str(right - left))
            chars[left + 1 : right] = str_num if right - left > 1 else []
            return left + (len(str_num) + 1 if right - left > 1 else 1)

        while right < len(chars):
            if chars[right] != left_char:
                left = right = _compress(left, right)
                left_char = chars[left]
            right += 1

        return _compress(left, right)


# OK 29%, 50%
