import re
def encode(string):
    string = string.lower()
    rez = [] 
    for character in string:
        if re.search("[a-z]", character):
            number = ord(character) - 96
            string = re.sub(character, str(number), string)
    return string
    
    """
    def encode(string):
      return ''.join(str(ord(c)-96) if c.isalpha() else c for c in string.lower())
    """
