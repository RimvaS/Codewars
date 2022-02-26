import re

def ohms_law(s):
    V, I, R = 0, 0, 0
    string = re.split(r" ",s)
    for x in string:
        if x[-1] == 'A':
            I = float(x[:-1])
        elif x[-1] == 'R':
            R = float(x[:-1])
        elif x[-1] == 'V':
            V = float(x[:-1])

    if V == 0:
        V = str(round(I * R, 6)) +'V'
        return V
    elif R == 0:
        R = str(round(V / I, 6)) +'R'
        return R
    elif I == 0:
        I = str(round(V / R, 6)) +'A'
        return I
    return '0.0V'
