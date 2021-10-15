n = int(input())
triangle = []
triangle.append([0])
for _ in range(n):
    triangle.append(list(map(int, input().split())))
maxTri = [[0]*n for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(i):
        if i == 1:
            maxTri[i][j] = triangle[i][j]
        if j == 0:
            maxTri[i][j] = maxTri[i-1][j] + triangle[i][j]
        if j == i-1:
            maxTri[i][j] = maxTri[i-1][j-1] + triangle[i][j]
        else:
            maxTri[i][j] = max(maxTri[i-1][j-1], maxTri[i-1][j]) + triangle[i][j]

print(max(maxTri[n]))