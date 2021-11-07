from collections import deque
T = int(input())
INF = "A"*10001
def makeNum(lst):
    return int(''.join(list(lst)))

def isSame(A,B):
    if A == B:
        return True
    else:
        return False

def makeStr(A):
    if A//1000:
        return str(A)
    elif A//100:
        return '0'+str(A)
    elif A//10:
        return '00'+str(A)
    return '000'+str(A)

def D(A):
    A = (A*2)%10000
    return A,'D'

def S(A):
    if A == 0:
        return 9999,'S'
    else:
        return A-1,'S'

def L(A):
    A = makeStr(A)
    return makeNum(A[1]+A[2]+A[3]+A[0]),'L'

def R(A):
    A = makeStr(A)
    return makeNum(A[3]+A[0]+A[1]+A[2]),'R'

def InDp(A,dp,past,now):
    #print("A",A,"dp[A]",dp[A])
    if dp[A] == INF:
        dp[A] = past+now
    elif len(dp[A]) > len(past+now):
        dp[A] = past+now
    # print("A:",A,"dp[A]:",dp[A], past+now)

visited = [False for _ in range(10000)]
    

for _ in range(T):
    a,b = map(int, input().split())
    A = makeStr(a)
    B = makeStr(b)
    dp = [INF for _ in range(10000)]
    dp[a] = ""
    visited[a] = True
    A = makeNum(A)
    q=deque([A])
    while not isSame(A,b):
        A = q.popleft()
        # print("std", A)
        d,dc = D(A)
        if not visited[d]:
            visited[d] = True
            InDp(d,dp,dp[A],dc)
        q.append(d)
        s,sc = S(A)
        if not visited[s]:
            visited[s] = True
            InDp(s,dp,dp[A],sc)
        q.append(s)
        l,lc = L(A)
        if not visited[l]:
            visited[l] = True
            InDp(l,dp,dp[A],lc)
        q.append(l)
        r,rc = R(A)
        if not visited[r]:
            visited[r] = True
            InDp(r,dp,dp[A],rc)
        
    print(dp[b])