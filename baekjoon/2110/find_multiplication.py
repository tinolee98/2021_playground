N,M = list(map(int,input().split()))
table = []
for _ in range(N):
    lst = list(input())
    table.append(lst)
#print(table)
def solution():
    maximum = -1
    size = []
    point = []
    # 우선 table 내의 요소들을 등차수열로 얻어내서 숫자들의 리스트를 만들고,
    # 만든 리스트 내의 수들을 제곱수인지 판단.
    for i in range(N):
        for j in range(M):
            point.append((i,j))
            size.append((i,j))
            size.append((i,-j))
            size.append((-i,j))
            size.append((-i,-j))
    size = list(set(size))
    #print(size)
    # (i,j)에서 나올 수 있는 경우들을 구함.
    tempResult = []
    for i,j in point:
        # (i,j)에서 (n,m)만큼 떨어지는 경우의 수 구하기
        for n,m in size:
            tempList = [(i,j)]
            #print("(",i,j,")","(",n,m,")")
            for k in range(1,max(N,M)):
                a,b = i + k*n, j + k*m
                #print(a,b)
                if not (0<=a<N and 0<=b<M) or (a,b) in tempList:
                    break
                else:
                    tempList.append((a,b))
            #print(tempList)
            temp = ''
            for a,b in tempList:
                temp += table[a][b]
                if temp not in tempResult:
                    tempResult.append(temp)
            #print(tempResult)
        #print("----")
            #     c = ''.join(table[a][b])
            # else:
            #     continue
            # if (a,b,c) not in tempList:
            #     tempList.append((a,b))
            # pass
    result = list(map(int, tempResult))
    for i in result:
        if int(i**(1/2))**2 == i:
            maximum = max(maximum,i)
    return maximum

print(solution())