def validate_hello(greetings):
    list = ('hello','ciao','salut','hallo','ahoj','czesc','hola')
    for i in range(len(list)):
        if list[i] in greetings.lower():
            return True
        else:
            pass
    return False
