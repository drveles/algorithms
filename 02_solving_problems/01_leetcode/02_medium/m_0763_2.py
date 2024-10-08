class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_indexes = {char:idx for idx, char in enumerate(s)}
        start = end = 0
        result = []

        for idx, char in enumerate(s):
            end = max(end, last_indexes[char])

            if end == idx:
                result.append(end - start + 1)
                start = end + 1
        
        return result
            