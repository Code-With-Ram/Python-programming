def findWater(array):
    count = 0
    i = 0
    j  = i + 1
    while i < len(array)-1:
        j  = i + 1
        while array[i] > array[j]:
            j+=1
            if j == len(array):
                i+=1
                j=i+1
            if j >= len(array):
                break
        if j == len(array):
            break
        total_area = min(array[i] , array[j]) * (j - i -1)
        print(array[i] , array[j] , total_area)        
        for x in range(i+1,j):
            total_area -= array[x]

        count+=total_area
        d = j - i
        i+= d
    return count



#l=  [3,0,0,2,0,4]
#l= [2,0,2]
l  =[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

l = [1 ,4 ,2 ,5 ,0 ,6 , 2 , 3, 4]
#l = [0,4,5,1]
#l = [3,0,3]
print(findWater(l))
