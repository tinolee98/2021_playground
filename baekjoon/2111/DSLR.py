from collections import deque
N = int(input())

def funcL(now):
    now = '0'*(4-len(now))+now
    now = list(now)
    now[0],now[1],now[2],now[3] = now[1],now[2],now[3],now[0]
    return int(''.join(now))

def funcR(now):
    now = '0'*(4-len(now))+now
    now = list(now)
    now[0],now[1],now[2],now[3] = now[3],now[0],now[1],now[2]
    return int(''.join(now))

def Str(now):
    now = str(now)
    return "0"*(4-len(now))+now

for _ in range(N):
    now, target = list(input().split())
    now = Str(now)
    target = Str(target)
    q = deque([(now, "")])
    #print(now, target)
    visited = [False for _ in range(10000)]
    visited[int(now)] = True
    finish = False
    while q:
        now, cmds = q.popleft()
        #print(now, cmds)
        # D: 두 배 만들기
        D = int(now)*2 if int(now)*2 < 10000 else int(now)*2%10000
        # S: 1을 빼기
        S = int(now)-1 if int(now)>0 else 9999
        # L: 자릿수를 왼쪽으로 이동
        L = funcL(now)
        # R: 자릿수를 오른쪽으로 이동
        R = funcR(now)
        for n,c in [(D,"D"), (S,"S"), (L, "L"), (R, "R")]:
            if Str(n) == target:
                print(cmds+c)
                finish = True
                break
            if not visited[n] and n not in q:
                visited[n] = True
                q.append((Str(n), cmds+c))
        if finish:
            break