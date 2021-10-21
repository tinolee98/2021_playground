N,M = list(map(int, input().split()))

numList = [0 for _ in range(M)]
index = 0
used = [False for _ in range(N)]

def solution(used, numList, index):
    if index == M:
        print(' '.join(list(map(str,numList))))
        return

    for i in range(N):
        if index == 0 or not used[i] and i+1 > numList[index-1]:
            used[i] = True
            numList[index] = i+1
            solution(used, numList,index+1)
            used[i] = False

solution(used, numList, index)