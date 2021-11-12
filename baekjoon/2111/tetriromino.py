N,M = list(map(int, input().split()))
nums = []
for _ in range(N):
    nums.append(list(map(int, input().split())))
#print(nums)

dij = [(1,0),(-1,0),(0,1),(0,-1)]

def DFS(nums,I,J,i,j,size,s):
    now = nums[i][j]
    if size == 4:
        return s+now
    result = 0
    for di,dj in dij:
        ci = i+di
        cj = j+dj
        if ci == I and cj == J:
            continue
        if 0<=ci<N and 0<=cj<M:
            result = max(result, DFS(nums, i,j,ci,cj,size+1,s+now))
    return result

def Mt(nums,i,j):
    if (i == 0 or i == N-1) and (j==0 or j==M-1):
        return 0
    result = nums[i][j]
    re = False
    for di,dj in dij:
        ci = i+di
        cj = j+dj
        if 0<=ci<N and 0<=cj<M:
            result += nums[ci][cj]
        else:
            re = True
    if re:
        return result
    else:
        reArr = []
        for di,dj in dij:
            ci = i+di
            cj = j+dj
            reArr.append(result-nums[ci][cj])
        return max(reArr)

visited = {}
result = 0
for i in range(N):
    for j in range(M):
        result = max(result, Mt(nums,i,j))
        result = max(result, DFS(nums,i,j,i,j,1,0))
print(result)