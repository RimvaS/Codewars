def trouble(x, t):
    n = 0
    i = 0
    while n < len(x)-1:
        if x[i] + x[i + 1] == t:
            x.pop(i + 1)
            i = i
        else:
            n += 1
            i += 1
    return x
