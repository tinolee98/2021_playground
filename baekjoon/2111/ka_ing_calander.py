T = int(input())

def GCD(M,N):
    #print(M,N)
    return GCD(N,M%N) if M%N != 0 else N

def Cal(M,N,Y,g):
    for i in range(Y):
        if  (N*i+g)//M*M == N*i+g:
            return i
    return -1

def Function(M,N,x,y):
    last = M*N // GCD(max(M,N), min(M,N))
    X = last//M
    Y = last//N
    answer = 0
    if x<y:
        temp = Cal(M,N,Y,y-x)
        if temp != -1:
            answer = temp * N + y
    else:
        temp = Cal(N,M,X,x-y)
        if temp != -1:
            answer = temp * M + x
    #print(answer)
    return answer if temp != -1 else temp

for _ in range(T):
    M,N,x,y = list(map(int, input().split()))
    print(Function(M,N,x,y))