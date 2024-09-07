class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        ctr = 0

        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                ctr += 1

        return ctr


# OK, 77% , 85%
