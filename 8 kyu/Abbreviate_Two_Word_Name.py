def abbrev_name(name):
    i = ''
    for x in name.split(' '):
        i +=  x.upper()[:1] +'.'           
    return i[:-1]
