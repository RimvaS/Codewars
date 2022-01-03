import numpy as np
def max_sum_between_two_negatives(arr):
    rez = []
    index = [i for i, x in enumerate(arr) if x < 0]
    for i in range(0,len(index)-1):
        indices = [index[i], index[i+1]]
        a = sum(arr[index[i]+1:index[i+1]])
        rez.append(a)
    return -1 if len(index) < 2 else max(rez)
    
