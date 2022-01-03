def mobile_keyboard(s):
    s = list(s)
    result = 0
    Data = {'a': 2,'b': 3,'c': 4,'d': 2,'e': 3,'f': 4, 
            'g': 2,'h': 3,'i': 4,'j': 2,'k': 3,'l': 4,
            'm': 2,'n': 3,'o': 4,'p': 2,'q': 3,'r': 4,
            's': 5,'t': 2,'u': 3,'v': 4,'w': 2,'x': 3,
            'y': 4,'z': 5,'*': 1,'#':1
           }
    for a in s:
        if a in Data.keys():
            result += Data.get(a)
        elif type(int(a)) == int:
            result += 1
        else:
            pass
    return result
