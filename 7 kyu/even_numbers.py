def even_numbers(arr,n):
    even=[]
    for i in range (0,len(arr)):
        if (arr[i] % 2 == 0):
            even.append(arr[i])
    return even[-n:]
