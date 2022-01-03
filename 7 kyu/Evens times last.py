def even_last(numbers): 
    ls = numbers[0::2]
    if numbers == []:
        return 0
    return sum(ls) * numbers[-1]
