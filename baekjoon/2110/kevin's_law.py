from collections import deque
INF = int(1e7)
N,M = list(map(int,input().split()))
relation = [[]for _ in range(N+1)]
for _ in range(M):
    a,b = list(map(int,input().split()))
    relation[a].append(b)
    relation[b].append(a)

minIndex = 0
result = INF
for i in range(1,N+1):
    visited = [False for _ in range(N+1)]
    dist = [INF for _ in range(N+1)]
    dist[i] = 0
    dist[0] = 0
    q = deque([(0,i)])
    while q:
        d, target = q.popleft()
        if not visited[target]:
            visited[target] = True
            for j in relation[target]:
                q.append((d+1,j))
        dist[target] = min(dist[target], d)
    if sum(dist) < result:
        minIndex = i
        result = sum(dist)
#print(result)
print(minIndex)
        
