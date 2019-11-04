from math import factorial
def join(s): 
  
    # initialization of string to "" 
    new = "" 
  
    # traverse in the string  
    for x in s: 
        new += x  
  
    # return string  
    return new 
      
  

def permutation(s,l = 0):
    permcount = -1
    if l!= 0:
        permcount = factorial(l)
    s = list(s)
    if len(s) == 0:
        print("Empty string")

    elif len(s)==1:
        return [s]

    elif len(s)>1:
        perm= []

        for i in range(len(s)):
            m = s[i]
            remlist = s[:i] +s[i+1:]
            for p in permutation(remlist):
                perm.append([m] + p)

    if permcount == len(perm):
        for i in range(len(perm)):
            perm[i] = join(perm[i])

    return perm
    


#print()
#print(permutation("RAM",3))

    
