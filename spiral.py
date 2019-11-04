a = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
  [1, 2, 3, 4],
]
# 0,0 0,1 0,2 0,3 1,3 2,3 3,3 3,2 3,1 3,0 2,0 1,0 1,1

def SolveMatrix(n, mat):
  
  k = 0
  l = 0
  m = n
  
  while k < m and l < n:

    for i in range(l, n):
      print(a[k][i], end=",")
    k+=1

    for i in range(k, m):
      print(a[i][n-1], end=",")
    n-=1

    for i in range(n-1, l-1, -1):
      print(a[m-1][i], end=",")
    m-=1

    for i in range(m-1, k-1, -1):
      print(a[i][l], end=",")
    l+=1
  
SolveMatrix(4, a)
