def ones_counter(inp):
    p = []
    s = 0
    for i in range(0,len(inp)):
        if inp[i] == 1:
            s += 1
        if inp[i] == 0 or i == len(inp)-1:
            p.append(s)
            s = 0
    p = [i for i in p if i != 0]
    return p
