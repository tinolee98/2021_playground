import heapq
import sys
N = int(input())
h = []
input = sys.stdin.readline
for _ in range(N):
    answer = 0
    n = int(input().rstrip())
    if n != 0:
        heapq.heappush(h,(abs(n),n))
    else:
        if len(h) > 0:
            a,answer = heapq.heappop(h)
        print(answer)