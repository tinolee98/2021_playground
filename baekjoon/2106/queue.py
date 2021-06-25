# 큐 구현하기

s = int(input())
q = []
size = 0
command = []
for i in range(s):
    command.append(list(map(str, input().split())))
for i in range(s):
    if command[i][0] == 'pop':
        if size == 0:
            print(-1)
        else:
            print(q[0])
            del(q[0])
            #for j in range(len(q)-1):
            #    q[j] = q[j+1]
            size -= 1
    elif command[i][0] == 'back':
        if size == 0:
            print(-1)
        else:
            print(q[-1])
    elif command[i][0] == 'size':
        print(size)
    elif command[i][0] == 'front':
        if size == 0:
            print(-1)
        else:
            print(q[0])
    elif command[i][0] == 'empty':
        if size == 0:
            print(1)
        else:
            print(0)
    else:
        x = int(command[i][1])
        q.append(x)
        size += 1
