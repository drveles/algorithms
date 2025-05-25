class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        left, right = 0, len(nums1)
        total_len = len(nums1) + len(nums2)
        half_len = (total_len + 1) // 2

        while left <= right:
            nums1_mid = (left + right) // 2
            nums2_mid = half_len - nums1_mid

            nums1_left = float('-inf') if nums1_mid == 0 else nums1[nums1_mid - 1] 
            nums2_left = float('-inf') if nums2_mid == 0 else nums2[nums2_mid - 1]
            nums1_right = float('inf') if nums1_mid == len(nums1) else nums1[nums1_mid]
            nums2_right = float('inf') if nums2_mid == len(nums2) else nums2[nums2_mid]

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if total_len % 2 == 0:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
                return max(nums1_left, nums2_left)

            if nums1_left > nums2_right:
                right = nums1_mid - 1
            else:
                left = nums1_mid + 1

        raise Exception('Incorrect input data')
