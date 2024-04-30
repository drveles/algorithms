class Solution:
    def maxDistToClosest(self, seats) -> int:
        longest_space = 0
        curr_space = seats.index(1)

        for seat in seats: 
            if seat: 
                longest_space, curr_space = max(math.ceil(curr_space / 2), longest_space), 0
            else:
                curr_space += 1

        return max(longest_space, curr_space)
    

if __name__ == "__main__":
    print(Solution().maxDistToClosest([1,1,1,1,1,1,1,0]))


# OK, 42%, 63%