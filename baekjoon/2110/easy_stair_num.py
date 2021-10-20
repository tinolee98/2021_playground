from copy import deepcopy
N = int(input())
e = [1 for _ in range(10)]
e[0] = 0

for i in range(N-1):
    temp = [0 for _ in range(10)]
    for j in range(10):
        if j == 0:
            temp[1] += e[j]
        elif j == 9:
            temp[8] += e[j]
        else:
            temp[j-1] += e[j]
            temp[j+1] += e[j]

    e = deepcopy(temp)
print(sum(e)%int(1e9))
    