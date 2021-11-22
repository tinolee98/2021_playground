N = int(input())
nums = list(map(int, input().split()))
dp = [1 for _ in range(N)]
last = nums[0]
for i, n in enumerate(nums):
    if i == 0:
        dp[0] = 1
        continue
    for j, m in enumerate(nums[:i]):
        if m < n:
            dp[i] = max(dp[i], dp[j]+1)
    # print(dp)
print(max(dp))