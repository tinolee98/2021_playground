N = int(input())

def FindMax(st,M):
    dp = [[0 for _ in range(M)] for _ in range(2)]
    for i in range(M):
        if i == 0:
            dp[0][i] = st[0][0]
            dp[1][i] = st[1][0]
            continue
        if i == 1:
            dp[0][i] = dp[1][i-1]+st[0][1]
            dp[1][i] = dp[0][i-1]+st[1][1]
            continue
        dp[0][i] = max(dp[1][i-1], dp[0][i-2], dp[1][i-2]) + st[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2], dp[1][i-2]) + st[1][i]
    maximum = max(max(dp[0]), max(dp[1]))
    return maximum
        

for _ in range(N):
    M = int(input())
    stickers = []
    for _ in range(2):
        stickers.append(list(map(int, input().split())))
    print(FindMax(stickers,M))
