from collections import deque
import collections

n,m,v = list(map(int,input().split()))
table = [[] for _ in range(n+1)]
for i in range(m):
    a,b = list(map(int,input().split()))
    table[a].append(b)
    if a not in table[b]:
        table[b].append(a)
for i in range(n+1):
    table[i].sort()
#print(table)
visited = [False for _ in range(n+1)]
#print(visited)

now = v
stack = []
result = []

def dfs(now, stack):
    result.append(now)
    visited[now] = True
    temp = sorted(table[now], reverse=True)
    stack += temp
    while stack:
        now = stack.pop()
        if (not visited[now]):
            visited[now] = True
            temp = sorted(table[now], reverse=True)
            stack += temp
            result.append(now)
    return result

dfsResult = dfs(now, stack)

now = v
queue = deque([])
result = []
visited = [False for _ in range(n+1)]

def bfs(now, queue):
    result.append(now)
    visited[now] = True
    queue += table[now]
    while queue:
        now = queue.popleft()
        if (not visited[now]):
            visited[now] = True
            queue += table[now]
            result.append(now)
    return result

bfsResult = bfs(now, queue)
print(' '.join(map(str,dfsResult)))
print(' '.join(map(str,bfsResult)))