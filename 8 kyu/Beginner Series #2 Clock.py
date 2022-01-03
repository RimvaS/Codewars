def past(h, m, s):
    rez = 0
    if 0 <= h <= 23: 
        rez += h * 3600000
    if 0 <= m <= 59:
        rez += m * 60000
    if 0 <= s <= 59:
        rez += s * 1000       
    return rez
