
def findCand(a):
    cand = [1] * len(a)
    
    for i in range(1,len(a)-1):
        if cand[i] == cand[i-1]:
            if a[i] > a[i-1]:
                cand[i]+=1
            elif a[i] < a[i-1]:
                cand[i-1]+=1
        if cand[i] == cand[i+1]:
            
            if a[i] > a[i+1]: 
                cand[i]+=1
            elif a[i] < a[i+1]: 
                cand[i+1]+=1
            
    
    return cand




a = [1,5,2,1]
#a = [1,2]
#a = [5 ,5, 4, 3, 2, 1]
print(findCand(a))
        
