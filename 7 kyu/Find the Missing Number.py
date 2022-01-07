def missing_no(nums):
    n = list(range(100, -1, -1))
    a = list(set(n) - set(nums))
    return a[0]
