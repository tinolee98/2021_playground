N,M = list(map(int, input().split()))

numList = [0 for _ in range(M)]
index = 0

def solution(numList, index):
    if index == M:
        print(' '.join(list(map(str,numList))))
        return

    for i in range(N):
        if index == 0 or numList[index-1] <= i+1:
            numList[index] = i+1
            solution(numList,index+1)

solution(numList, index)