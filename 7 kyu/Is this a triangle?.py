def is_triangle(a, b, c):
    l = [a, b, c]
    l.sort()
    return True if int(str(l[0])) + int(str(l[1])) > int(str(l[2])) else False

