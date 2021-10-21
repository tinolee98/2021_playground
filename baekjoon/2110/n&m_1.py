N,M = list(map(int, input().split()))

check = [True] + [False for _ in range(N)]
index = 1
num = [0 for _ in range(M+1)]

def func(check, num, index):
    if index == M+1:
        result = ' '.join(list(map(str,num[1:])))
        print(result)
        return
    for i in range(1,N+1):
        if not check[i]:
            num[index] = i
            check[i] = True
            func(check, num, index+1)
            check[i] = False


func(check, num, index)