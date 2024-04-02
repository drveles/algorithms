class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        flag = False
        test_set = set()

        for el in nums:
            if el in test_set:
                flag = True
                break
            test_set.add(el)

        return flag

#OK
#57% time, 65% mem