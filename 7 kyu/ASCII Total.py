def uni_total(s):
    arr = list(s)
    result = 0
    
    for i in arr: 
        result += ord(i)
        
    return 0 if s == '' else result
    
    
    """
    def uni_total(string):
    return sum(map(ord, string))
    """
