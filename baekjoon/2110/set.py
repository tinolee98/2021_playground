import sys
N = int(input())
cmds = []
input = sys.stdin.readline
Set = [0 for _ in range(21)]
for _ in range(N):
    cmd = list(input().rstrip().split())
    if cmd[0] == "add":
        cmd[0] = 0
    elif cmd[0] == "remove":
        cmd[0] = 1
    elif cmd[0] == "check":
        cmd[0] = 2
    elif cmd[0] == "toggle":
        cmd[0] = 3
    elif cmd[0] == "all":
        cmd[0] = 4
    elif cmd[0] == "empty":
        cmd[0] = 5

    if len(cmd) == 1:
        if cmd[0] == 4:
            Set = [1 for _ in range(21)]
        else:
            Set = [0 for _ in range(21)]
        continue
    c,n = cmd
    n = int(n)
    if c == 0:
        Set[n] = 1
    elif c == 1:
        Set[n] = 0
    elif c == 2:
        r = 1 if Set[n] == 1 else 0
        print(r)
    elif c == 3:
        if Set[n] == 0:
            Set[n] == 1
        else:
            Set[n] == 0