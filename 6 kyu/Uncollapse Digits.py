def uncollapse(digits):
    a = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in a:
        digits = digits.replace(i, i + " " )
    digits = digits[:-1]
    return digits
