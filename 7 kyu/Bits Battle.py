def bits_battle(numbers):
    odds = []
    evens = []
    for x in numbers: 
        if x % 2 == 0: 
            evens.append(bin(x)[2:])
        else:
            odds.append(bin(x)[2:])
    a = "".join(odds)
    b = "".join(evens)
    if a.count('1') > b.count('0'): 
        return 'odds win'
    elif a.count('1') < b.count('0'): 
        return 'evens win'
    else:
        return 'tie' 
    
