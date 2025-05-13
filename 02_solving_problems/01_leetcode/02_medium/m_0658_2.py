class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # осознал О(n) решение. можно же начать с двух сторон массива и выбрасывать тот хвост, что больше
        if len(arr) == k:
            return arr

        left, right = 0, len(arr) - 1

        while right - left + 1 > k:
            if abs(arr[left] - x) <= abs(arr[right] - x):
                right -= 1
            else:
                left += 1

        return arr[left:right + 1]
