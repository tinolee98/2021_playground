from collections import deque
import sys
N = int(input())
table = [[] for _ in range(N)]
input = sys.stdin.readline
for i in range(N):
    lst = list(map(int, input().rstrip().split()))
    for n in range(N):
        if lst[n] == 1:
            table[i].append(n)
#print(table)
for i in range(N):
    q= deque(table[i])
    visited = [False for _ in range(N)]
    #visited= [True for _ in range(i+1)] + [False for _ in range(N-i-1)]
    #print(visited)
    while q:
        now = q.popleft()
        if not visited[now]:
            visited[now] = True
            for p in table[now]:
                if p not in q:
                    q.append(p)
                if p not in table[i]:
                    table[i].append(p)
    #table[i] = list(set(table[i]))
result = []
for i in range(N):
    lst = []
    for j in range(N):
        if j in table[i]:
            lst.append('1')
        else:
            lst.append('0')
    print(' '.join(lst))