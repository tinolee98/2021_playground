N = int(input())
for _ in range(N):
    M = int(input())
    closet = []
    keys = []
    result = 1
    for _ in range(M):
        name, kind = list(map(str,input().split()))
        if kind in keys:
            closet[keys.index(kind)] += 1
        else:
            keys.append(kind)
            closet.append(1)
    for n in closet:
        result *= n+1
    print(result-1)