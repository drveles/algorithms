def myQuicksort(arr):
    len_arr = len(arr)
    if len_arr < 2:
        return arr
    
    opora = arr.pop(len_arr // 2)
    less = []
    greater = []

    for id1 in range(len_arr - 1):
        if arr[id1] < opora:
            less.append(arr[id1])
        else:
            greater.append(arr[id1])
    
    return(myQuicksort(less) + [opora] + myQuicksort(greater))
