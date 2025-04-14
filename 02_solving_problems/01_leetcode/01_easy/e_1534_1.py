class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        result = 0

        for idx0 in range(len(arr)):
            idx1 = idx0 + 1
            while idx1 < len(arr):
                idx2 = idx1 + 1
                while idx2 < len(arr):
                    if (
                        abs(arr[idx0] - arr[idx1]) <=  a 
                        and abs(arr[idx1] - arr[idx2]) <= b
                        and abs(arr[idx0] - arr[idx2]) <= c
                    ):
                        result += 1
                    idx2 += 1
                idx1 += 1

        return result
