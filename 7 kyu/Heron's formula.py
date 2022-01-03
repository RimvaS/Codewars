import math

def heron(a,b,c):
    s = (a+b+c)/2
    p = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return round(p, 2)
