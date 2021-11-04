import sys
from collections import deque
N,M,H = list(map(int, input().split()))
input = sys.stdin.readline
tomatoes = []
q = deque()
for h in range(H):
    lst = []
    for m in range(M):
        lst.append(list(map(int, input().rstrip().split())))
        for n in range(N):
            if lst[m][n] == 1:
                q.append((h,m,n))
    tomatoes.append(lst)
# print(tomatoes)
# print(q)

direction = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

while q:
    h,m,n= q.popleft()
    for dh,dm,dn in direction:
        ch = h+dh
        cm = m+dm
        cn = n+dn
        if 0<=ch<H and 0<=cm<M and 0<=cn<N and tomatoes[ch][cm][cn] == 0:
            q.append((ch,cm,cn))
            tomatoes[ch][cm][cn] = tomatoes[h][m][n] + 1
        # print(q)
answer = 0
for h in tomatoes:
    for m in h:
        for n in m:
            if n == 0:
                print(-1)
                exit()
        answer = max(answer, max(m))
print(answer-1)