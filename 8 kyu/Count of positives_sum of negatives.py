def count_positives_sum_negatives(arr):
    a = sum([1 for x in arr if x > 0])
    b = sum([x for x in arr if x < 0])
    c = []
    c.append(a)
    c.append(b)
    return c if arr != [] else []
