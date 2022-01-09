import re
def printer_error(s):
    x = re.sub('[a-m]','',s)
    return f'{len(x)}/{len(s)}'
