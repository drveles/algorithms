def binary(array, k):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = right - left // 2

        if array[mid] == k:
            return mid

        if array[mid] < k:
            left = mid + 1
        else:
            right = mid - 1

    return -1
