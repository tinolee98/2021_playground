import sys
N = int(input())
cmds = []
input = sys.stdin.readline
Set = [0 for _ in range(21)]
for _ in range(N):
    cmd = list(input().rstrip().split())
    if len(cmd) == 1:
        if cmd[0] == "all":
            Set = [1 for _ in range(21)]
        else:
            Set = [0 for _ in range(21)]
        continue
    c,n = cmd
    n = int(n)
    if c == "add":
        Set[n] = 1
    elif c == "remove":
        Set[n] = 0
    elif c == "check":
        print(1 if Set[n]==1 else 0)
    elif c == "toggle":
        if Set[n] == 1:
            Set[n] = 0 
        else:
            Set[n] = 1


#for cmd in cmds:
    #print(cmd)
    #print(Set)