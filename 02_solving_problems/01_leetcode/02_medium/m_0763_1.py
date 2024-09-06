class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []
        last_char_idx = {}
        start_part = max_position = 0

        for idx, char in enumerate(s):
            last_char_idx[char] = idx

        for idx, char in enumerate(s):
            max_position = max(max_position, last_char_idx[char])
            if max_position == idx:
                result.append(idx - start_part + 1)
                start_part = idx + 1

        return result


# OK, 91%, 72%
