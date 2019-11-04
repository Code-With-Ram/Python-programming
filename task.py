l = [2,2,0,4,0,8]
l = [2 ,2 ,0 ,4, 0, 2]
for i in range(len(l)-1):
    if l[i] == 0:
        continue
    if l[i] == l[i+1]:
        l[i] = l[i] * 2
        l[i+1]  = 0
z = []
i=  0
j = len(l)
while i < j:
    if l[i] == 0:
        z.append(l.pop(i))
        j-=1
        i-=1
    i+=1
l +=z

print(l)
