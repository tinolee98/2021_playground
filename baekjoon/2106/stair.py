# 계단 오르기

h = int(input())
stair = []
for _ in range(h):
    stair.append(int(input()))
stair = stair[::-1]
i=1
result = stair[0]
check = [1]
while i < h:
    if i+2 < h:
        if i+3 == h and stair[i] < stair[i+1]+stair[i+2]:
            result += (stair[i+1]+stair[i+2])
            break
        elif stair[i]+stair[i+2] > stair[i+1]:
            result += (stair[i]+stair[i+2])
            check += [i+1, i+3]
            i += 3
        elif stair[i+1] > stair[i]:
            result += stair[i+1]
            check.append(i+2)
            i += 2
        else:
            result += stair[i]
            check.append(i+1)
            i += 1
    else:
        result += stair[-1]
        check.append(h)
        break
print(check)
print(result)
