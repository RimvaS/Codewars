def array_madness(a,b):
    if len(a) and len(b) >= 1:
            squaresb: int = 0
            squaresa: int = 0
            for x in range(len(a)):
                squaresa = squaresa + a[x] * a[x]
            for y in range(len(b)):
                squaresb = squaresb + b[y] * b[y] * b[y]
            return True if squaresa > squaresb else False
    else:
        return False      
    return False
