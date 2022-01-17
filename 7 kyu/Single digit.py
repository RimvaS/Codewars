def single_digit(n):
    while n > 9:
        k = 0
        for i in list(bin(n)[2:]):
            k += int(i)
        n = k
    return  n
