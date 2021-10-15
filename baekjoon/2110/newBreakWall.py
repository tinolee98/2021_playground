from collections import deque
N,M = list(map(int, input().split()))
way = []
for _ in range(N):
    lst = list(map(int, list(input())))
    way.append(lst)
print(way)
visited = [[[False]*M for _ in range(N)]for _ in range(2)]
noWall = 0
broken = 1
visited[noWall][0][0] = True
visited[broken][0][0] = True

dx = [1,0,-1,0]
dy = [0,-1,0,1]
alreadyBreak = False
q = deque([(0,0)])
while q:
    x,y = q.popleft()
    print(x,y)
    for i in range(4):
        cx = x+dx[i]
        cy = y+dy[i]
        if 0<=cx<M and 0<=cy<N :
            if way[cy][cx] != 1 and not visited[noWall][cy][cx]:
                visited[noWall][cy][cx] = True
                if (cx,cy) not in q:
                    q.append((cx,cy))
                if way[cy][cx] != 0:
                    way[cy][cx] = min(way[cy][cx], way[y][x]+1)
                else:
                    way[cy][cx] = way[y][x]+1
print(way)
    