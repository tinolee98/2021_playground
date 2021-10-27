import sys
N,M = list(map(int, input().split()))
input = sys.stdin.readline
note = {}
for _ in range(N):
    site, pw = list(input().rstrip().split())
    note[site] = pw
for _ in range(M):
    site = input().rstrip()
    print(note[site])
