def buy(x,arr): 
    for i in range(0,len(arr)): 
        for c in range(1,len(arr)):
            if i != c:
                if arr[i] + arr[c] == x:
                    return [i,c]
    return None
