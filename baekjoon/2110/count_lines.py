import sys
from collections import deque
N,M = list(map(int, input().split()))
input = sys.stdin.readline
lines = [[] for _ in range(N+1)]
for _ in range(M):
    start,end = list(map(int,input().split()))
    lines[start].append(end)
    lines[end].append(start)
#print(lines)

visited = [False for _ in range(N+1)]
def DFS(now,stack):
    while stack:
        if not visited[now]:
            visited[now] = True
            now = stack.pop()
            for n in lines[now]:
                if n not in stack and not visited[n]:
                    stack.append(n)
            DFS(now,stack)
        else:
            now = stack.pop()

def BFS(now):
    q = deque([now])
    while q:
        now = q.popleft()
        if not visited[now]:
            visited[now] = True
            for i in lines[now]:
                if not visited[i] and i not in q:
                    q.append(i)
    return 1

    

count = 0
for i in range(1,N+1):
    if not visited[i]:
        count += BFS(i)
print(count)