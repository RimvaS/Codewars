def solution(stones):
    a = 0
    for x in range(0,len(stones)-1):
        if stones[x] == stones[x+1]:
            a +=1 
    return a
