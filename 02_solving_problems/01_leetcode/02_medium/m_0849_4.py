class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:
        last = maxx = 0

        for num in seats:
            if num:
                maxx = max(maxx, last)
                last = 0
                continue
            last += 1

        return max(seats.index(1), ceil(maxx / 2), last)
