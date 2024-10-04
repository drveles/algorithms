class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:             
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        total_len = len(nums1) + len(nums2)
        left, right = 0, len(nums1)

        while left <= right:
            mid1 = (left + right) // 2
            mid2 = (total_len + 1) // 2 - mid1

            min1 = nums1[mid1 - 1] if mid1 > 0 else float("-inf")
            min2 = nums2[mid2 - 1] if mid2 > 0 else float("-inf")
            max1 = nums1[mid1] if mid1 < len(nums1) else float("inf")
            max2 = nums2[mid2] if mid2 < len(nums2) else float("inf")

            if max(min1, min2) <= min(max1, max2):
                if total_len % 2:
                    return max(min2, min1)
                else:
                    return (min(max1, max2) + max(min2, min1)) / 2
            elif min1 > max2:
                right = mid1 - 1
            else:
                left  = mid1 + 1
