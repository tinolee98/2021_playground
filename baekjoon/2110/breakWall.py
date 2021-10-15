from copy import *

from collections import deque
N,M = list(map(int, input().split()))
INF = int(1e7)
way = []
for _ in range(N):
    lst = list(map(int,list(input())))
    way.append(lst)
#print(way)

for i in range(N):
    for j in range(M):
        if i+j != 0 and way[i][j] == 0:
            way[i][j] = INF

dx = [1,0,-1,0]
dy = [0,1,0,-1]
wall = []

def canArrive(way):
    queue = deque([(0,0)])
    visited = [[False]*M for _ in range(N)]
    while queue:
        #print(queue)
        x,y = queue.popleft()
        visited[y][x] = True
        for i in range(4):
            cx = x+dx[i]
            cy = y+dy[i]
            if 0<=cx<M and 0<=cy<N and not visited[cy][cx]:
                if way[cy][cx] != 1:
                    way[cy][cx] = min(way[cy][cx], way[y][x] + 1)
                    if (cx,cy) not in queue:
                        queue.append((cx,cy))
                else:
                    wall.append((cx,cy))

    #print(way)
    if visited[N-1][M-1]:
        del visited
        return way
    del visited
    return []

def breakWall(wall, way):
    #print("특정 부분만!")
    canBreakWall = deepcopy(wall)
    minLen = INF
    #print("wallList",canBreakWall)
    for wx,wy in canBreakWall:
        tempWay = deepcopy(way)
        tempWay[wy][wx] = INF
        tempCanArriveResult = canArrive(tempWay)
        if tempCanArriveResult and tempWay[N-1][M-1] != INF:
            #print(tempWay)
            #print(wx,wy)
            minLen = min(minLen, tempWay[N-1][M-1])
        del tempWay
    del canBreakWall
    if minLen == INF:
        if N*M == 1:
            return 1
        return -1
    return minLen+1

def checkAllCase(way):
    #print("all check!")
    wallList = []
    for n in range(N):
        for m in range(M):
            if way[n][m] == 1:
                wallList.append((n,m))
    return breakWall(wallList,way)


testWay = deepcopy(way)
canArriveResult = canArrive(testWay)
if canArriveResult:
    result = checkAllCase(way)
else:
    result = breakWall(wall, way)
print(result)
