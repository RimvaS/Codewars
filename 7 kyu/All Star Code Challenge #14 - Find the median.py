def median(array):
    half = len(array) // 2
    array.sort()
    if not len(array) % 2:
        return (array[half - 1] + array[half]) / 2.0
    return array[half]    
    
