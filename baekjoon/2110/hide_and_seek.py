
from collections import deque

N,K = list(map(int, input().split()))

INF = int(2e5)
visited = [False for _ in range(INF+1)]
count = [INF for _ in range(INF+1)]
q = deque([N])
count[N] = 0

def BFS():
    while q:
        now = q.popleft()
        visited[now] = True
        a,b,c = now-1, now+1, now*2
        for i in [a,b,c]:
            if 0<=i<=INF and not visited[i]:
                count[i] = min(count[i], count[now]+1)
                q.append(i)
    return count[K]
print(BFS())