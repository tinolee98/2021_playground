n,m = list(map(int,input().split()))
N = [i for i in range(n-m+1,n+1)]
M = [i for i in range(1,m+1)]
result = 1
for i in N:
    result *= i
for i in M:
    result //= i
print(result)