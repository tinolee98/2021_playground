N = int(input())
stair = []
for _ in range(N):
    stair.append(int(input()))
step1 = [stair[0]]
step2 = [0]
for i in range(1,len(stair)):
    if i == 1:
        step1.append(stair[i-1]+stair[i])
        step2.append(stair[i])
    else:
        step1.append(step2[i-1]+stair[i])
        step2.append(max(step1[i-2], step2[i-2])+stair[i])
    # print(step1, step2)
print(max(step1[N-1], step2[N-1]))