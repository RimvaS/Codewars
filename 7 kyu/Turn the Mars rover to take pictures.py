def turn(current, target):
    if current == 'N' and target == 'E': return 'right'
    if current == 'N' and target == 'W': return 'left'
    if current == 'S' and target == 'E': return 'left'
    if current == 'S' and target == 'W': return 'right'
    if current == 'E' and target == 'N': return 'left'
    if current == 'E' and target == 'S': return 'right'
    if current == 'W' and target == 'S': return 'left'
    if current == 'W' and target == 'N': return 'right'
    return 
  
  """
  def turn(_c, _t):
    return 'right' if 'NESWN'.find(_c + _t) > -1 else 'left'
  """
