graph = {'A':['B','F'],
         'B':['H'],
         'F':[],
         'C':[],
         'D':['C','I','E'],
         'E':['I'],
         'G':['A','B','C'],
         'H':[],
         'I':['C'],
         'J':['E']
         }


def dag(g):
    visited = []
    for n in g.keys():
        DAG(n,g,visited)
    print(visited)
def DAG(n,g,visited):
    for v in g[n]:
        DAG(v,g,visited)
    if n not in visited:
        visited.append(n)
    if g[n]==[]:
        return
    

                  
dag(graph)
