from collections import deque
N,M = list(map(int, input().split()))
table = []
INF = int(1e7)
for _ in range(N):
    lst = list(map(int, input()))
    table.append(lst)

for i in range(N):
    for j in range(M):
        if table[i][j] == 1:
            table[i][j] = INF

q = deque([(0,0)])
table[0][0] = 1
dx = [1,0,-1,0]
dy = [0,-1,0,1]
visited = [[False]*M for _ in range(N)]

def BFS():
    while q:
        x,y = q.popleft()
        visited[y][x] = True
        for i in range(4):
            cx = x+dx[i]
            cy = y+dy[i]
            if 0<=cx<M and 0<=cy<N and table[cy][cx] != 0:
                if not visited[cy][cx] and (cx,cy) not in q:
                    q.append((cx,cy))
                table[cy][cx] = min(table[cy][cx], table[y][x] + 1)
        #print(q)
        #print(table)
        
BFS()
print(table[N-1][M-1])