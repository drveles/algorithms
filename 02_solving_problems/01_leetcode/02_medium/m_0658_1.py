from typing import List
import bisect

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        len_arr = len(arr)
        start_id = bisect.bisect_left(arr, x)
        end_id = bisect.bisect_right(arr, x)
        if start_id == end_id:
            start_id -= 1  
        if start_id > -1 and arr[start_id] == x:
            res.insert(0, arr[start_id])
            k -= 1
            start_id -= 1
        while k:
            if k and start_id > -1:
                res.insert(0, arr[start_id])
                k -= 1
                start_id -= 1
            if k and end_id < len_arr:
                res.append(arr[end_id])
                k -= 1
                end_id += 1

        return res
            


if __name__ == "__main__":
    # print(Solution().findClosestElements([1,2,3,4,5], 4, 3))
    print(Solution().findClosestElements([0,1,1,1,2,3,6,7,8,9], 9, 4))

#WA