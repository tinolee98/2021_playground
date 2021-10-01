N = int(input())
temp = (1,1,1)

for _ in range(N):
    a,b,c = temp
    A = a+b+c
    B = a+c
    C = a+b
    temp = (A,B,C)
print(A%9901)