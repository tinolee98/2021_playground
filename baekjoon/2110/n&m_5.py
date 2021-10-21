N,M = list(map(int, input().split()))

numList = [0 for _ in range(M)]
index = 0
used = {}

lst = list(map(int, input().split()))
lst.sort()
for n in lst:
    used[n] = False

def solution(used, numList, index):
    if index == M:
        print(' '.join(list(map(str,numList))))
        return

    for i in lst:
        if not used[i]:
            numList[index] = i
            used[i] = True
            solution(used, numList,index+1)
            used[i] = False

solution(used, numList, index)