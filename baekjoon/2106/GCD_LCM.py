# 최소공배수, 최대공약수 문제

def GCD(a,b):
    a,b = max(a,b), min(a,b)
    if a%b == 0:
        return b
    else:
        a,b = b, a%b
        return GCD(a,b)

a,b = map(int, input().split())
g = GCD(a,b)
l = int(a*b/g)
print(g)
print(l)