class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_space = 0
        curr_space = seats.index(1)

        for seat in seats:
            if seat:
                max_space = max((curr_space + 1) // 2, max_space)
                curr_space = 0
            else:
                curr_space += 1

        return max(max_space, curr_space)


# OK, 51%, 52%
