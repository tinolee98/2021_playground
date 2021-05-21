# 스택 구현: push, pop, size, empty, top
n = int(input())
lst = []
stack = []
for j in range(n):
    lst.append(list(map(str, input().split())))
for j in range(n):
    if lst[j][0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif lst[j][0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            temp = stack.pop()
            print(temp)
    elif lst[j][0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif lst[j][0] == 'size':
        print(len(stack))
    else:
        stack.append(lst[j][1])
    #print(stack)