def shortcut( s ):
    return s.translate({ord(i): None for i in 'aeiou'})
