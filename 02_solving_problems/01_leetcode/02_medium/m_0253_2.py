# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
# find the minimum number of conference rooms required.

# [[0, 30],[5, 10],[15, 20]] -> 2

import heapq

class Solution():
    def minRoomRequeired(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        heap = []

        heapq.heappush(heap, intervals[0][1])

        for start, end in intervals[1:]:
            if start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, end)

        return len(heap)


if __name__ == "__main__":
    s = Solution()

    print(s.minRoomRequeired([[0, 30],[5, 10],[15, 20]]))
    print(s.minRoomRequeired([[0, 30],[5, 10],[15, 20], [1,30]]))