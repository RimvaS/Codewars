def make_valley(arr):
    arr.sort(reverse=True)
    a = arr[0::2]
    b = arr[1::2]
    b.sort()
    a.extend(b)
    return a
