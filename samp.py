s = '1'
state = 0

for x in s:
    
    if x == '0':
        if state == 1:
            state = 0
        elif state == 2:
            
    elif x == '1':
        if state == 0:
            state = 1

if state == 0:
    print("YES")
else:
    print("NO")
