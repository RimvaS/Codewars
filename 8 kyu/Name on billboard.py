def billboard(name, price=30):
    a: int = 0 
    total: int = 0 
    while a < price:
        total+= len(name) 
        a += 1
    return total
    
