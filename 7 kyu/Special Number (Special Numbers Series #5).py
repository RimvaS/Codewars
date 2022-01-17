def special_number(number):
    for i in list(str(number)):
        if int(i) not in list(range(0,6)):
            return 'NOT!!' 
    return 'Special!!'
	
