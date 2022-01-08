def zombie_shootout(zombies, distance, ammo):
    if zombies > ammo and distance * 2 > ammo:
        return f"You shot {ammo} zombies before being eaten: ran out of ammo."    
    elif zombies * 0.5 > distance: 
        return f"You shot {distance * 2} zombies before being eaten: overwhelmed."
    return f"You shot all {zombies} zombies."
  
  
  """
  def zombie_shootout(z, r, a):
    s = min(r*2, a)
    return f"You shot all {z} zombies." if s>=z else f"You shot {s} zombies before being eaten: { 'overwhelmed' if s==2*r else 'ran out of ammo' }."
  """
