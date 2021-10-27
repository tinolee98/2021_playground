import sys
N = int(input())
input = sys.stdin.readline
nums = list(map(int, input().rstrip().split()))
asc = sorted(list(set(nums)))
nd = {}
for i,n in enumerate(asc):
    nd[n] = i
#print(asc)
red = []
for n in nums:
    r = nd[n]
    red.append(str(r))
print(' '.join(red))