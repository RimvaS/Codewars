def find_needle(haystack):
    for i in range(len(haystack)):
        if haystack[i] == 'needle':
            return f'found the needle at position {i}'
