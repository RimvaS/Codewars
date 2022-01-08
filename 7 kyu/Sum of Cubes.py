def sum_cubes(n):
    cubes = list(range(1, n+1))
    return sum(i*i*i for i in cubes)
    
"""
def sum_cubes(n):
    return sum(i**3 for i in range(0,n+1))

"""
