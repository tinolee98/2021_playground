from collections import deque
N = int(input())
br = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
for _ in range(N-1):
    a,b = list(map(int, input().split()))
    br[a].append((a,b))
    br[b].append((b,a))
parents = [0 for _ in range(N+1)]
parents[1] = -1
q = deque(br[1])
visited[1] = True
while q:
    parent, child = q.popleft()
    if not visited[child]:
        parents[child] = parent
        visited[child] = True
        q += br[child]
    # print(q)
for p in parents[2:]:
    print(p)