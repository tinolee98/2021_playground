N = int(input())
keys = []
children = []
for i in range(N):
    lst = list(input().split())
    keys.append(lst[0])
    children.append((lst[1],lst[2]))

def Cycle(now,position):
    result = ""
    i = keys.index(now)
    left, right = children[i]
    if position == 0:
        result = now
    if left != '.':
        result += Cycle(left,position)
    if position == 1:
        result += now
    if right != '.':
        result += Cycle(right,position)
    if position== 2:
        result += now
    return result   

for j in range(3):
    print(Cycle(keys[0], j))

