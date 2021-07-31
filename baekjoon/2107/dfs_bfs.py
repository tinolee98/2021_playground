# DFS, BFS 수행 결과 출력하기

def DFS(v):
    #print("DFS")
    arrDfs.append(v)
    for i in maps[v]:
        if i != 0 and i not in arrDfs:
            DFS(i)

def BFS(q):
    #print("BFS")
    while len(q) != 0:
        #print(q)
        v = q.pop(0)
        if v != 0 and v not in arrBfs:
            arrBfs.append(v)
            q += maps[v]


n,m,v = map(int, input().split())
maps = [[0] * (n+1) for _ in range(n+1)]
arrDfs = []
arrBfs = []
check = [0] * (n+1)
check[1] = 1
#print(maps)
for _ in range(m):
    a, b = map(int, input().split())
    maps[a][b] = b
    maps[b][a] = a
#print(maps)
DFS(v)
print(" ".join(map(str,arrDfs)))
check = [0] * (n+1)
check[1] = 1
arrBfs.append(v)
BFS(maps[v])
print(" ".join(map(str,arrBfs)))