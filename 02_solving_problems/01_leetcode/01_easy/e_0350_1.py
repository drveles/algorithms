class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        dict2 = {}

        for num in nums2:
            dict2[num] = dict2.get(num, 0) + 1
        

        for num in nums1:
            if num in dict2:
                res.append(num)
                dict2[num] = dict2[num] - 1
                if dict2[num] == 0:
                    del dict2[num]

        return res

#OK, 81, 71