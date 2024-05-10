class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = sorted(nums1 + nums2)
        len_res = len(res)
        if len_res % 2 != 0:
            return res[len_res // 2]
        else:
            return float((res[len_res // 2 - 1] + res[len_res // 2]) / 2.0)
        
#OK 50%, 30%