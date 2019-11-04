def isNumber(s):
    try:        
        k = s[0]
        s = s[1:]
    except IndexError:
        return True
    return ( (k.isdigit() or k == '.') and isNumber(s))

s = '112.10.001'
print(isNumber(s))
