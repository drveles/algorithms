class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        curr_interval = intervals[0]
        result = []

        for iid in range(1, len(intervals)):
            if intervals[iid][0] > curr_interval[1]:
                result.append(curr_interval)
                curr_interval = intervals[iid]
            else:
                curr_interval[1] = max(curr_interval[1], intervals[iid][1])
        result.append(curr_interval)

        return result


# OK, 84%, 35%