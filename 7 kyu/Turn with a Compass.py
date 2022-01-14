def direction(facing, turn):
    compass = {'N':0,'NE':45,'E':90,'SE':135,'S':180,'SW':225,'W':270,'NW':315}
    if turn > 0:
        rez = compass.get(facing)+turn
    else: 
        rez = turn
    if rez < 0:
        while rez < 0:
            rez += 360
        rez += compass.get(facing)
    while rez > 360:
        rez -=360 
    if rez == 360:
        rez = 0
    for key, value in compass.items():
        if value == rez:
            return key          
    return facing 
