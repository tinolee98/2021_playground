N,r,c = list(map(int, input().split()))
size = 2**N

#table = [[0 for _ in range(size)] for _ in range(size)]
#print(table)
now = 0
a,b = 0,0
def z(n,now,a,b):
    next = 4**(n-1)
    nextPoint = 2**(n-1)
    if n == 1:
        if a == r and b == c:
            print(now)
        elif a==r and b+1 == c:
            print(now+1)
        elif a+1 == r and b == c:
            print(now+2)
        elif a+1 == r and b+1 == c:
            print(now+3)
        exit()
    else:
        if r < a+nextPoint and c < b+nextPoint:
            z(n-1,now,a,b)
        elif r >= a+nextPoint and c < b+nextPoint:
            z(n-1,now+2*next,a+nextPoint,b)
        elif r < a+nextPoint and c >= b+nextPoint:
            z(n-1,now+next,a,b+nextPoint)
        else:
            z(n-1,now+3*next,a+nextPoint,b+nextPoint)
z(N,now,a,b)
#print(table)