def binary(array, k):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if array[mid] == k:
            return mid

        if array[mid] < k:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    assert binary([1, 2, 3, 4, 5], 3) == 2
    assert binary([], 1) == -1
    assert binary([1, 2, 4, 5], 3) == -1
    assert binary([1, 2, 3, 4, 5], -1) == -1
    assert binary([1, 2, 3], 4) == -1
    assert binary([0, 1, 2, 3], 0) == 0
    assert binary((0, 1, 2, 3), 3) == 3
