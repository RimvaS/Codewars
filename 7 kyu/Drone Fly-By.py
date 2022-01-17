def fly_by(lamps, drone):
    n = len(lamps) - len(drone) 
    if len(drone) > len(lamps):
        n = len(lamps)
        drone = ''
        for i in range(n):
            drone += 'o'
        return drone
    else:
        drone = drone.replace('=','o')
        drone = drone.replace('T','o')

        for i in range(n): 
            drone += 'x'
    return drone
    
    
    """
    def fly_by(lamps, drone):
    return lamps.replace('x', 'o', len(drone) )
    """
