def sum_of_intervals(intervals):
    lengh = set()
    for a, b in intervals:
        for i in range(a, b):
            lengh.add(i)    
    return len(lengh)
