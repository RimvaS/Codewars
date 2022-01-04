def divisions(n, divisor):
    a = 0
    k = 0
    while a != 1:
        if n / divisor > 1:
            n = n / divisor
            k += 1
        else: 
            a = 1
    return k
