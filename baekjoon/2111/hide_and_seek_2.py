subin, brother = list(map(int, input().split()))
INF = 100001
dp = [INF]*INF
cnts = [0]*INF
dp[subin] = 0
visited = [False]*INF
toFind = [(subin,1)]
cont = True
l = 1
if subin == brother:
    print(0)
    print(1)
    exit()
while cont:
    lst = []
    temp = []
    for n,cnt in toFind:
        lst += [(n,n-1,cnt), (n,n+1,cnt), (n,2*n,cnt)]
    toFind = []
    for now,next,cnt in lst:
        if 0<=next<INF:
            cnts[next] += cnt
            dp[next] = min(dp[now]+1, dp[next])
            if not visited[next]:
                visited[next] = True
                temp.append(next)
            if next == brother:
                cont = False 
    for i in temp:
        toFind.append((i,cnts[i]))
    # print(cnts[:brother+1])
print(dp[brother])
print(cnts[brother])
