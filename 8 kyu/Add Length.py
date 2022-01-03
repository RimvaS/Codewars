import re
def add_length(str_):
    a = []
    b = re.split("\s", str_)
    for i in range(len(b)):
        c = b[i] + " " + str(len(b[i]))
        a.append(c)
    return a
