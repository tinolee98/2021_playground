from collections import deque
T = int(input())

def makeStr(A):
    if A//1000:
        return str(A)
    elif A//100:
        return '0'+str(A)
    elif A//10:
        return '00'+str(A)
    return '000'+str(A)

INF = "."*10001

for _ in range(T):
    a,b = list(map(int, input().split()))
    visited = [False for _ in range(10000)]
    cmds = [INF for _ in range(10000)]
    cmds[a] = ""
    print(a,b)
    q = deque([a])
    while q:
        n = q.popleft()
        now = cmds[n]
        N = makeStr(n)
        D = ((a*2)%10000,"D")
        S = ((a-1 if a > 0 else 9999), "S")
        L = (int(N[1:]+N[0]), "L")
        R = (int(N[3]+N[:3]), "R")
        testLst = [D,S,L,R]
        for num, c in testLst:
            pass
        if cmds[b] != INF:
            break
