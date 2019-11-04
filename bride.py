
d = {'a':1,'b':2,'c':5,'d':8}
left = ['a','b','c','d']
right =[]
cost = 0
n=4
i= 0 
while len(right)!=n:
    if i%2 ==0:
        right.insert(0,left.pop(0))
        x = left.pop()
        cost+=d[x]
        right.append(x)
        
    else:
        x = left.pop()
        cost+=d[x]
        right.append(x)
        right.insert(0,left.pop())
    i+=1
    left.sort()
    right.sort()
    x =right.pop(0)
    cost+= d[x]
    left.insert(0,x)
    left.sort()
    right.sort()
    print(left)

print(cost,left,right)
    
        
        
