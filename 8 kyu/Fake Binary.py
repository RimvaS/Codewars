import re
def fake_bin(x):
    a = re.sub('[1-4]','0',x)
    b = re.sub('[5-9]','1',a)
    return b
