def descending_order(num):
    numlist = [str(x) for x in str(num)]
    numlist.sort(reverse = True)  
    res = int("".join(numlist))
    return res
