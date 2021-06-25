# dfs 문제
import sys
sys.setrecursionlimit(10**6)
"""def dfs(m,i,j):
    #print(i,j)
    m[i][j] = 0
    if i > 0 and m[i-1][j] == 1:
        dfs(m,i-1,j)
    if i < len(m)-1 and m[i+1][j] == 1:
        dfs(m,i+1,j)
    if j > 0 and m[i][j-1] == 1:
        dfs(m,i,j-1)
    if j < len(m[0])-1 and m[i][j+1] == 1:
        dfs(m,i,j+1)"""

dx = [1,0,-1,0]
dy = [0,1,0,-1]
def dfs(m,i,j):
    m[i][j] = 0
    for k in range(4):
        x = i+dx[k]
        y = j+dy[k]
        if -1 < x < len(m) and -1 < y < len(m[0]) and m[x][y] == 1:
            #print("x y",x,y)
            dfs(m,x,y)



s = int(input())
Map = [[]for _ in range(s)]
for i in range(s):
    x,y,c = map(int,input().split())
    Map[i] = [[0]*y for _ in range(x)]
    for j in range(c):
        a,b = map(int,input().split())
        Map[i][a][b] = 1

for m in Map:
    count = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 1:
                dfs(m,i,j)
                #print(i,j)
                count += 1
            #print(m)
    print(count)