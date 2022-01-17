import math
def wallpaper(l, w, h):
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven",
               "eight", "nine", "ten", "eleven", "twelve","thirteen", "fourteen",
               "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
    rez = math. ceil((2*(l*h+w*h) / 5.2) *1.15)
    return numbers[rez] if l*w*h > 0 else numbers[0]
