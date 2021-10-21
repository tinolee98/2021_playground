import sys
N,M = list(map(int,input().split()))

input = sys.stdin.readline
neverHeard = []
neverSeen = []
for _ in range(N):
    neverHeard.append(input().rstrip())
for _ in range(M):
    neverSeen.append(input().rstrip())

result = set.intersection(set(neverHeard),set(neverSeen))
#print(result)

result = list(result)
result.sort()
print(len(result))
for e in result:
    print(e)
