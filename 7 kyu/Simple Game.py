def game(n, m): 
    print(n,m)
    if n == 1 or m == 2:
        return 'second'
    if n % 2 != 0:
        return 'first'
    if (m * n) % 2 == 0:
        return 'second'
    return 'first'
