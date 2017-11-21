def merge_lists(arr1, arr2):
    i = k = n = 0
    arr = [0] * (len(arr1) + len(arr2))
    while i < len(arr1) and k < len(arr2):
        if arr1[i] <= arr2[k]:
            arr[n] = arr1[i]
            i += 1
            n += 1
        else:
            arr[n] = arr2[k]
            k += 1
            n += 1
    while i < len(arr1):
        arr[n] = arr1[i]
        i += 1
        n += 1
    while k < len(arr2):
        arr[n] = arr2[k]
        k += 1
        n += 1
    return arr
