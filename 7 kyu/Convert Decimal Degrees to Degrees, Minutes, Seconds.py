def convert(degrees):
    result = [int(degrees), int(degrees * 60 % 60), round(degrees * 3600 % 60)]
    return result if result[2] else result[:2] if result[1] else result[:1]
