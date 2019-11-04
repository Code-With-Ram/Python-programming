a = [
  [1, 2, 3, 4],
  [12, 13, 14, 5],
  [11, 16, 15, 6],
  [10, 9, 8, 7],
    ]

a = [
  [1, 2, 3, 4, 5],
  [14, 15, 16,17, 6],
  [13, 20, 19,18, 7],
  [12, 11, 10, 9,8],
    ]

# 0,0 0,1 0,2 0,3 1,3 2,3 3,3 3,2 3,1 3,0 2,0 1,0 1,1

def SolveMatrix(n,m, mat):
  
  imax = n
  jmax = m
  imin = 0
  jmin = 0
  i = 0
  while jmin < n//2:
    
    for j in range(jmin,jmax):
        print(a[i][j],end=',')
    imin+=1
    for i in range(imin,imax):
        print(a[i][j],end=',')
    jmax-=1

    for j in range(jmax-1,jmin-1,-1):
        print(a[i][j],end=',')
    imax-=1

    for i in range(imax-1,imin-1,-1):
        print(a[i][j],end=',')
    jmin+=1
    


      
SolveMatrix(4,5, a)
