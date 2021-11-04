N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))
coins.sort(reverse=True)
count = 0
for coin in coins:
    count += K//coin
    K %= coin
print(count)