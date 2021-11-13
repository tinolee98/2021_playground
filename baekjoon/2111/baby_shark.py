from collections import deque
from copy import deepcopy
N = int(input())
fishes = [[] for _ in range(8)]
fishSpot = []
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] == 9:
            now = (i,j,0)
        elif temp[j] != 0:
            fishes[temp[j]].append((i,j,temp[j]))
    fishSpot.append(temp)
size = 2
eatenFishes = 0

q = deque([now])
result = 0

def BFS(i,j,size,canEat,fishSpot):
    dij = [(1,0),(-1,0),(0,1),(0,-1)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[i][j] = True
    q = deque([(i,j)])
    tempQ = deque()
    result = []
    dist = 1
    while q:
        i,j = q.popleft()
        for di,dj in dij:
            ci = i+di
            cj = j+dj
            if 0<=ci<N and 0<=cj<N and not visited[ci][cj] and (fishSpot[ci][cj] <= size or fishSpot[ci][cj] == 9):
                visited[ci][cj] = True
                tempQ.append((ci,cj))
                if (ci,cj,fishSpot[ci][cj]) in canEat:
                    result.append((ci,cj,fishSpot[ci][cj],dist))
        if not q:
            if result:
                return result
            q = deque(deepcopy(tempQ))
            dist += 1
            tempQ = []
    return result

while q:
    i,j,s = q.popleft()   # 지금 위치
    canEat = []
    for lst in fishes[:size]:
        canEat += lst
    nextSpot = 0
    if not canEat:
        break
    dist = 0
    nextSpot= BFS(i,j,size,canEat,fishSpot)
    nextSpot.sort()
    if not nextSpot:
        break
    x,y,s,dist = nextSpot[0]
    q.append((x,y,s))
    fishes[s].remove((x,y,s))
    result += dist
    eatenFishes += 1
    if size == eatenFishes:
        eatenFishes = 0
        size +=1
print(result)

