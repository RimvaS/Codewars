def two_oldest_ages(ages):
    b = max(ages)
    ages.remove(b)
    c = max(ages)
    return [c, b]
