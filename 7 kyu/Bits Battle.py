
def bits_battle(numbers):
    odds = []
    evens = []
    for x in numbers: 
        if x % 2 == 0: 
            evens.append(bin(x)[2:])
        else:
            odds.append(bin(x)[2:])
    a = "".join(odds)
    b = "".join(evens)
    if a.count('1') > b.count('0'): 
        return 'odds win'
    elif a.count('1') < b.count('0'): 
        return 'evens win'
    else:
        return 'tie' 
    
  """
  
  def bits_battle(a):
  odds, evens = sum([bin(i).count('1') for i in a if i % 2]), sum([bin(i).count('0') - 1 for i in a if i % 2 == 0])
  return 'odds win' if odds > evens else 'evens win' if evens > odds else 'tie'
  
  """
