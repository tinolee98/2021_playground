from collections import deque
N = int(input())
colors = []
for _ in range(N):
    colors.append(list(input()))
rgVisited = [[False for _ in range(N)] for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]

dij = [(1,0), (-1,0), (0,1), (0,-1)]

def RG(q,rgVisited,std):
    if std != 'B':
        std = ['R','G']
    while q:
        i,j = q.popleft()
        rgVisited[i][j] = True
        for di,dj in dij:
            ci = i+di
            cj = j+dj
            if 0<=ci<N and 0<=cj<N and not rgVisited[ci][cj] and colors[ci][cj] in std and (ci,cj) not in q:
                q.append((ci,cj))

def Normal(q, visited,std):
    while q:
        i,j = q.popleft()
        visited[i][j] = True
        for di,dj in dij:
            ci = i+di
            cj = j+dj
            if 0<=ci<N and 0<=cj<N and not visited[ci][cj] and colors[ci][cj] == std and (ci,cj) not in q:
                q.append((ci,cj))

rgCnt = 0
cnt = 0
for i in range(N):
    for j in range(N):
        if not rgVisited[i][j]:
            RG(deque([(i,j)]), rgVisited,colors[i][j])
            rgCnt += 1
        if not visited[i][j]:
            Normal(deque([(i,j)]), visited, colors[i][j])
            cnt += 1
print(cnt, rgCnt)