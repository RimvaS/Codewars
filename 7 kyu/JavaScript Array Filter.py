def check_even(number):
    if number % 2 == 0:
          return True  
    return False

def get_even_numbers(arr):
    return list(filter(check_even, arr))
    
    
"""
def get_even_numbers(arr):
    return list(filter(lambda x: x % 2 == 0, arr))
"""
