class SummaryRanges:
    def __init__(self):
        self.elements = set()
        
    def addNum(self, value: int) -> None:
        self.elements.add(value)

    def getIntervals(self) -> List[List[int]]:
        result = []
        seen = set()
        for el in self.elements:
            if el in seen:
                continue
            left = right = el
            while el - 1 in self.elements:
                seen.add(el - 1)
                left = el - 1
                el -= 1
            while el + 1 in self.elements:
                seen.add(el + 1)
                right = el + 1
                el += 1
            seen.add(el)
            idx = bisect.bisect(result, [left, right])
            result.insert(idx, [left, right])
        return result
