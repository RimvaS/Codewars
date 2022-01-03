def sum_array(arr):
    if arr == None:
        return 0
    if arr != [] and len(arr) > 2:
        a = min(arr)
        b = max(arr)
        c = arr.remove(a)
        c = arr.remove(b)
        if arr == []:
            return 0
        rez = sum(arr)
    else:
        return 0
    return rez
