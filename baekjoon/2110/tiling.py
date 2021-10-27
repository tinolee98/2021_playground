N = int(input())

tiles = [1,1]
for i in range(2,N+1):
    tiles.append(tiles[i-2]*2 + tiles[i-1])
print(tiles[N]%10007)