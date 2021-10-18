from collections import deque
N = int(input())
A = list(map(int, input().split()))
opNum = list(map(int, input().split()))

maxDp = {tuple(opNum):A[0]}
minDp = {tuple(opNum):A[0]}

q = deque([tuple(opNum)])
#print(q)
result = []
while q:
    oper = q.popleft()
    n = N -sum(oper)
    #print(maxDp)
    #print(oper, n)
    for i, op in enumerate(oper):
        temp = []+list(oper)
        if op > 0:
            #print(n)
            if i == 0:
                past = maxDp[tuple(temp)] + A[n]
            elif i == 1:
                past = maxDp[tuple(temp)] - A[n]
            elif i == 2:
                past = maxDp[tuple(temp)] * A[n]
            elif i == 3:
                past = int(maxDp[tuple(temp)] / A[n])
            temp[i] -= 1
            q.append(tuple(temp))
            if tuple(temp) not in maxDp:
                maxDp[tuple(temp)] = past
            else:
                maxDp[tuple(temp)] = max(maxDp[tuple(temp)], past)
            if sum(temp) == 0:
                result.append(past)
                result = list(set(result))
q = deque([tuple(opNum)])

while q:
    oper = q.popleft()
    n = N -sum(oper)
    #print(minDp)
    #print(oper, n)
    for i, op in enumerate(oper):
        temp = []+list(oper)
        if op > 0:
            #print(n)
            if i == 0:
                past = minDp[tuple(temp)] + A[n]
            elif i == 1:
                past = minDp[tuple(temp)] - A[n]
            elif i == 2:
                past = minDp[tuple(temp)] * A[n]
            elif i == 3:
                past = int(minDp[tuple(temp)] /A[n])
            temp[i] -= 1
            q.append(tuple(temp))
            if tuple(temp) not in minDp:
                minDp[tuple(temp)] = past
            else:
                minDp[tuple(temp)] = min(minDp[tuple(temp)], past)
            if sum(temp) == 0:
                result.append(past)
                result = list(set(result))
#print("max",maxDp)
#print("min",minDp)
#print(result)
print(max(result))
print(min(result))