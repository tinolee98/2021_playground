from collections import deque
N,M = list(map(int, input().split()))
table = []
oneList = []
for i in range(N):
    temp = list(input())
    table.append(temp)
    for j in range(len(temp)):
        if temp[j] == "1":
            oneList.append((i,j))

start = (0,0)
end = (N-1,M-1)

print(oneList)