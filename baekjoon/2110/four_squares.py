N = int(input())
n = int(50000**(1/2))
nums = [i**2 for i in range(1,n+1)]
INF = 50001
counts = [INF for _ in range(50001)]
counts[0] = 0
counts[1] = 1
for i in range(N+1):
    for n in nums:
        if i+n <= N:
            counts[i+n] = min(counts[i] + 1, counts[i+n])
print(counts[N])