N,K = list(map(int, input().split()))
things = []
dp = [0 for _ in range(K+1)]
for _ in range(N):
    w,v = list(map(int, input().split()))
    # print("----")
    if w <= K and v > 0:
        #check = []
        for i in range(len(dp)-1,-1,-1):
            if dp[i] != 0 and i+w <= K:# and i not in check:
                dp[i+w] = max(dp[i] + v, dp[i+w])
                #dp[i+w] = dp[i]+v
                #check.append(i+w)
            # print(dp)
        dp[w] = max(dp[w],v)
    # for i in range(K+1):
    #     if dp[i] != 0:
    #         print(i,dp[i])
    # print("------")
print(max(dp))