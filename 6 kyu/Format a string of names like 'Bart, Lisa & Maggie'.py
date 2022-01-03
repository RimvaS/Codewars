def namelist(namelist):
    b: str = ''
    for x in range(len(namelist)):
        for i,j in namelist[x].items():
            if x == 0:
                b = j
            elif x == len(namelist)-1:
                b += ' & ' + j 
            else:
                b += ', ' + j
    return b
