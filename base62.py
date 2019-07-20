b62 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def base62to10(base62):
    global b62
    length = len(base62)
    base10 = 0
    for i in range(length):
        ID = b62.index(base62[i])*(62**(length-i-1))
        base10 += ID
    return base10

def base10to62(base10):
    global b62
    temp =[]
    string = ''    
    while base10> 0:
        remainder = base10 % 62
        temp.insert(0,remainder)
        base10 = base10//62
    for i in temp:
        string += b62[i]
    return string

