def factors(number):
    _factors = []
    for i in range(1,number + 1):
        if number % i == 0:
            _factors.append(i)
    return _factors


def are_coprime(n,m):    
    same_values = set(factors(n)) & set(factors(m))
    print(same_values)
    if len(same_values) == 1:
        return True
    return False
