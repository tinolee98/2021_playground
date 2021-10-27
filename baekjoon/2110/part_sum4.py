import sys
N,M = list(map(int, input().split()))
input = sys.stdin.readline
nums = list(map(int, input().rstrip().split()))
partSum = [0]
for n in nums:
    partSum.append(partSum[-1]+n)
parts = []
for _ in range(M):
    parts.append(tuple(map(int, input().rstrip().split())))

for start, end in parts:
    print(partSum[end] - partSum[start-1])