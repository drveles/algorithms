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
            seen.add(el)
            left = right = el
            while el - 1 in self.elements:
                el -= 1
                seen.add(el)
                left = el
            while el + 1 in self.elements:
                el += 1
                seen.add(el)
                right = el
            idx = bisect.bisect(result, [left, right])
            result.insert(idx, [left, right])
        return result
