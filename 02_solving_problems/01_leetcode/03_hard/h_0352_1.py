class SummaryRanges:
    def __init__(self):
        self.array = []
        
    def addNum(self, value: int) -> None:
        idx = bisect.bisect(self.array, value)
        self.array.insert(idx, value)

    def getIntervals(self) -> List[List[int]]:
        if not self.array:
            return []

        result = []
        left = right = self.array[0]
        for _, value in enumerate(self.array):
            if value - 1 > right:
                result.append([left, right])
                left = value
            right = value
        result.append([left, right])
        return result
