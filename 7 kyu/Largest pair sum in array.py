def largest_pair_sum(numbers): 
    numbers.sort()
    return numbers[-2] + numbers[-1]
