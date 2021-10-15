target = int(input())
n = int(input())
broken = list(map(int,input().split()))
buttons = [i for i in range(10)]
for i in broken:
    buttons.remove(i)
now = 100
print(buttons)
withoutZero = buttons.copy()
if 0 in buttons:
    withoutZero.remove(0)
targetList = list(map(int,list(str(target))))
print(targetList)

if len(buttons) == 0:

    exit()

l = len(targetList)
l1 = ['1' for _ in range(l-1)]
l1 = int(''.join(l1))
l3 = ['1' for _ in range(l)]
l3 = int(''.join(l3))
if 0 not in buttons:
    l2 = ['1' for _ in range(l)]
    l4 = ['1' for _ in range(l+1)]
else:
    l2 = ['1'] + ['0' for _ in range(l-1)]
    l4 = ['1'] + ['0' for _ in range(l)]
l2 = int(''.join(l2))
l4 = int(''.join(l4))
l1 *= max(withoutZero)
l2 *= min(withoutZero)
l3 *= max(withoutZero)
l4 *= min(withoutZero)
print(l1,l2,l3,l4)

lst = [l1,l2,l3,l4]

def solution(target):
    small = []
    big = []
    tempList = targetList.copy()
    for i in targetList:
        if i in buttons:
            small.append(str(i))
            big.append(str(i))
            tempList.remove(i)
        else:
            break
    #print(tempList)
    temp,length = tempList[0],len(tempList)-1
    #print(temp,length)
    for i in range(len(buttons)):
        if temp < min(buttons):
            break
        elif temp < max(buttons):
            break
        if buttons[i] < temp < buttons[i+1]:
            a,b = buttons[i], buttons[i+1]
            break
    #print(a,b)
    small.append(str(a))
    big.append(str(b))
    for i in range(length):
        small.append(str(max(buttons)))
        big.append(str(min(buttons)))
    small = int(''.join(small))
    big = int(''.join(big))
    #print(small,big)
    return min(target-small+len(targetList), big-target+len(targetList))

if target in lst:
    print("exactly")
    print(len(str(target)))
elif target == now:
    print(0)
elif l1 < target < l2:
    print("l1,l2")
    print(min(target-l1+len(str(l1)), l2-target+len(str(l2))))
elif l2<target<l3:
    print("l2,l3")
    print(solution(target))
else:
    print("l3,l4")
    print(min(target-l3+len(str(l3)), l4-target+len(str(l4))))

# 뭔가 재귀적으로 해야할 것 같은 느낌인데, 아직 명확하게 코드를 짜진 못하겠네.