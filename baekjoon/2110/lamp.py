N,M = list(map(int, input().split()))

lamps = [[] for _ in range(N)]
for i in range(N):
    lst = list(input())
    lamps[i] += list(map(int, lst))
K = int(input())
#print(lamps)

def findMax():
    tempLamps = []
    for lst in lamps:
        countZero = lst.count(0)
        if countZero <= K and (countZero%2) == (K%2):
            tempLamps.append(lst)
    maxNum = 0
    for lst in tempLamps:
        tempMax = 0
        for lst2 in tempLamps:
            if lst == lst2:
                tempMax += 1
        maxNum = max(maxNum, tempMax)
    return maxNum

print(findMax())
