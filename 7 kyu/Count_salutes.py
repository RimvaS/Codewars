def count_salutes(hallway):
    b = hallway.replace('-', '')
    b = list(b)
    rez = 0
    for x in range(0,len(b)-1):
        for i in range(1,len(b)):
            if b[x] + b[i] == '><' and i > x:
                rez += 2
    return rez
