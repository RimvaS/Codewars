def max_sequence(arr):
    max,a=0,0
    for x in arr:
        a+=x
        print(a)
        if a<0:a=0
        if a>max:max=a
    else:       
        return max
