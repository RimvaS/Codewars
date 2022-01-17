def peak(arr):
    rez = []
    for i,j in enumerate(arr):
        left = sum(arr[0:i])
        right = sum(arr[i+1:len(arr)])
        if left == right: 
            rez.append(i)
    return -1 if rez == [] else rez[0]
