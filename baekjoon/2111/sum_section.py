import sys
N,M = list(map(int, input().split()))
input = sys.stdin.readline
dp = [[0 for _ in range(N)] for _ in range(N)]
nums = []
for i in range(N):
    lst = list(map(int, input().rstrip().split()))
    nums.append(lst)
for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:
            dp[i][j] = nums[i][j]
        elif i == 0:
            dp[i][j] = dp[i][j-1]+nums[i][j]
        elif j == 0:
            dp[i][j] = dp[i-1][j]+nums[i][j]
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + nums[i][j]
# for d in dp:
#     print(d)

for _ in range(M):
    x1,y1,x2,y2 = map(lambda x: x-1, list(map(int, input().rstrip().split())))
    A = dp[x2][y2]
    B = dp[x2][y1-1] if y1-1>=0 else 0
    C = dp[x1-1][y2] if x1-1>=0 else 0
    D = dp[x1-1][y1-1] if x1-1>=0 and y1-1>=0 else 0
    print(A-B-C+D)