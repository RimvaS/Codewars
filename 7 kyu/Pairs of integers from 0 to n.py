def generate_pairs(n):
    a = list(range(n+1))
    rez = []
    for i in range(0,len(a)):
        for x in range(0,len(a)):
            if x >= i: 
                c = [i,x]
                rez.append(c)
    return rez
