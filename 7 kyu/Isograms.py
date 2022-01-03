def is_isogram(string):
    a = set(string.upper())
    return len(a) == len(string)
