import sys
from collections import deque
INF = int(1e10+1)
N = int(input())
M = int(input())
input = sys.stdin.readline
line = [[] for _ in range(N+1)]
for _ in range(M):
    p1, p2, dist = list(map(int, input().rstrip().split()))
    line[p1].append((p2,dist))
start, target = list(map(int, input().rstrip().split()))
dst = [INF]*(N+1)
dst[start] = 0
visited = [False]*(N+1)
visited[start] = True
q = deque([start])
while q:
    now = q.popleft()
    visited[now] = True
    for next, l in line[now]:
        if dst[next] > dst[now]+l:
            dst[next] = dst[now]+l
            if next not in q:
                q.append(next)
print(dst[target])