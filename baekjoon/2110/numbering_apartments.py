from collections import deque
N = int(input())
m = []
for _ in range(N):
    lst = input()
    lst = list(map(int, lst))
    m.append(lst)
visited = [[False]*N for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,-1,0,1]

def BFS(n,x,y):
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()
        if m[y][x] != 0 and not visited[y][x]:
            visited[y][x] = True
            m[y][x] = n
            for k in range(4):
                cx = x + dx[k] 
                cy = y + dy[k]
                if 0<=cx<N and 0<=cy<N:
                    q.append((cx,cy))
        #print(q)
n = 1
for i in range(N):
    for j in range(N):
        if not visited[j][i] and m[j][i] != 0:
            BFS(n,i,j)

            n+=1
result = [0 for _ in range(n)]
for i in range(N):
    for j in range(N):
        if m[j][i] ==0:
            continue
        result[m[j][i]] += 1

result.pop(0)
result.sort()

print(len(result))
if len(result) == 0:
    print(0)
else:
    for i in result:
        print(i)