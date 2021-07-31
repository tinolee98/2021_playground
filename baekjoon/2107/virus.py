# 바이러스 / DFS 이용하기

def DFS(current, connect, check):
    for c in connect[current]:
        if c == 0 or check[c] == 1:
            pass
        else:
            check[c] = 1
            DFS(c,connect,check)


node = int(input())
line = int(input())

connect = [[0] * (node+1) for _ in range(node+1)]
check = [0] * (node+1)
#for i in range(node):
#    connect[i][i] = 1
#print(connect)
for i in range(line):
    n,m = map(int, input().split())
    connect[n][m] = m
    connect[m][n] = n

print(connect)

DFS(1,connect, check)
print(check)
check[1] = 0
print(sum(check))
