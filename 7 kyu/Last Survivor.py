def last_survivor(letters, coords): 
    l = list(letters)
    for i in range(len(coords)): 
        del(l[coords[i]])
    return "".join(l)    
