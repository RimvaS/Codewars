import math
import re
def century(year):
    if re.findall("[0-5][0-9]00", str(year)):
        return round(year / 100)
    else:
        return int((year / 100)+1)
