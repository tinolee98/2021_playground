N = int(input())
wine = []
for _ in range(N):
    wine.append(int(input()))
dp = [0 for _ in range(N)]

def drink(i):
    if i == 0:
        dp[i] = wine[i]
    elif i == 1:
        dp[i] = wine[i-1]+wine[i]
    elif i == 2:
        dp[i] = max(wine[i-2], wine[i-1]) + wine[i]
    elif i == 3:    
        dp[i] = max(dp[i-2], dp[i-3]+wine[i-1]) + wine[i]
    else:    
        dp[i] = max(dp[i-2], dp[i-3]+wine[i-1],dp[i-4]+wine[i-1]) + wine[i]
for i in range(N):
    drink(i)
#print(dp)
print(max(dp))
