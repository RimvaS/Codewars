def max_multiple(divisor, bound):
    while bound > 0:
        if bound % divisor == 0:
            return bound
        bound -= 1
    return 
  
  """
  def max_multiple(divisor, bound):
    return bound - (bound % divisor)
  """
