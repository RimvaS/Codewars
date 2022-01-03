import math
def get_positions(n):
    print(n)
    return (math.ceil(n % 3), math.ceil(n // 3)% 3, math.ceil(n // 9)% 3)
