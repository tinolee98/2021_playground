import sys
from collections import deque
input = sys.stdin.readline
A,B = list(map(int, input().rstrip().split()))

q = deque([(A,1)])
while q:
    A,cnt = q.popleft()
    if A == B:
        print(cnt)
        exit()
    if A*2 <= B:
        q.append((A*2, cnt+1))
    if A*10 +1 <= B:
        q.append((A*10+1, cnt+1))
print(-1)