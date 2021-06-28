# RGB 거리에서 페인트칠을 하는 비용의 최솟값 구하기

n = int(input())
cost = [[] for _ in range(n)]
for i in range(n):
    lst = list(map(int,input().split()))

    cost[i] += lst

a,b,c = 0,0,0
for i in range(n):
    A = [b+cost[i][0], c+cost[i][0]]
    B = [a+cost[i][1], c+cost[i][1]]
    C = [a+cost[i][2], b+cost[i][2]]
    #print(A,B,C)
    a,b,c = min(A),min(B),min(C)
print(min(a,b,c))