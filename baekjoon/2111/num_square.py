N,M = list(map(int, input().split()))

maxL = max(N,M)

s = []
for _ in range(N):
    s.append(list(input()))
#print(s)

def Check(i,j,size):
    result = 0
    for n in range(size,maxL):
        if i+n < N and j+n < M:
            if s[i][j] == s[i+n][j] and s[i][j] == s[i][j+n] and s[i][j] == s[i+n][j+n]:
                result = n+1
    return result
answer = 0
for i in range(N):
    for j in range(M):
        answer = max(answer, Check(i,j,answer-1))
print(answer**2)