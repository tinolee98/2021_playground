from collections import deque

INF = int(1e7)

n,m = list(map(int, input().split()))
table = [[] for _ in range(m)]
for i in range(m): 
    tomatoes = list(map(int, input().split()))
    table[i] += tomatoes
visited = [[False] * n for _ in range(m)]

queue = deque()

for i in range(m):
    for j in range(n):
        if table[i][j] == 1:
            visited[i][j] = True
            queue.append((i,j,0))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

hasZero = False
for i in range(m):
    if 0 in table[i]:
        hasZero = True

impossible = False

for y in range(m):
    for x in range(n):
        check = 0
        for i in range(4):
            X,Y = x+dx[i], y+dy[i]
            if X in range(n) and Y in range(m):
                if table[Y][X] == -1:
                    check += 1
            else:
                check += 1
        if check == 4 and table[Y][X] != -1:
            impossible = True
            #print(y,x)
            break
    if impossible:
        break
            

if not hasZero:
    print(0)
elif impossible:
    print(-1)
else:
    while queue:
        y,x,now = queue.popleft()
        for i in range(4):
            X,Y = x+dx[i], y+dy[i]
            if X in range(n) and Y in range(m) and table[Y][X] != -1 and not visited[Y][X]:
                visited[Y][X] = True
                table[Y][X] = -1
                queue.append((Y,X,now+1))
        #print(queue)
        #print(visited)
    print(now)