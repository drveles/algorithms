class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:             
        total_len = len(nums1) + len(nums2)
        left1 = left2 = 0
        prev_median = curr_median = 0

        while left1 + left2 < (total_len) // 2 + 1:
            prev_median = curr_median
            if left1 < len(nums1) and left2 < len(nums2):
                if nums1[left1] < nums2[left2]:
                    curr_median = nums1[left1]
                    left1 += 1
                else:
                    curr_median = nums2[left2]
                    left2 += 1
            elif left1 < len(nums1):
                curr_median = nums1[left1]
                left1 += 1
            else:
                curr_median = nums2[left2]
                left2 += 1

        if total_len % 2:
            return curr_median
        else:
            return (curr_median + prev_median) / 2

