N,M = list(map(int, input().split()))

numList = [0 for _ in range(M)]
index = 0

def solution(numList, index):
    if index == M:
        print(' '.join(list(map(str,numList))))
        return

    for i in range(N):
        numList[index] = i+1
        solution(numList,index+1)

solution(numList, index)