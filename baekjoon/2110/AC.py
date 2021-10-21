N = int(input())

def Check(command, n, lst):
    reverse = False
    for c in command:
        if c == 'R':
            reverse = True if not reverse else False
        elif c == 'D':
            if len(lst) == 0:
                print("error")
                return
            elif reverse:
                lst.pop()
            else:
                lst.pop(0)
    result = '['
    if reverse:
        for i in range(len(lst)-1,-1,-1):
            result += lst[i]
            if i != 0:
                result += ','
    else:
        for i in range(len(lst)):
            result += lst[i]
            if i != len(lst)-1:
                result += ','
    result += ']'
    print(result)

commandList = []
nList = []
lstList = []

for _ in range(N):
    command = list(input())
    n = int(input())
    lst = list(input())
    lst = lst[1:len(lst)-1]
    lst = ''.join(lst)
    lst = lst.split(',')
    result = []
    for e in lst:
        if e.isnumeric():
            result.append(e)
    commandList.append(command)
    nList.append(n)
    lstList.append(result)


for i in range(N):
    Check(commandList[i], nList[i], lstList[i])