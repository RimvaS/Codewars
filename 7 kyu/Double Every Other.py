def double_every_other(lst):
    for i in range(0,len(lst)):
        if i % 2 != 0:
            lst[i] *= 2
    return lst
  
  
