class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []

        if not firstList or not secondList:
            return result

        first = 0
        second = 0

        while first < len(firstList) and second < len(secondList):
            if firstList[first][0] > secondList[second][1]:
                second += 1
            elif secondList[second][0] > firstList[first][1]:
                first += 1
            else:
                result.append(
                    [
                        max(firstList[first][0], secondList[second][0]),
                        min(firstList[first][1], secondList[second][1]),
                    ]
                )
                if firstList[first][1] < secondList[second][1]:
                    first += 1
                else:
                    second += 1

        return result
