class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = list()

        indexes = dict()
        for idx, ch in enumerate(s):
            indexes[ch] = idx
        
        start = end = 0
        for idx, ch in enumerate(s):
            end = max(indexes[ch], end)
            if end == idx:
                result.append(end - start + 1)
                start = idx + 1

        return result
