n = int(input())
arr = []
for i in range(n):
    a,b = list(map(int, input().split()))
    arr.append((a,b))
result = []

def solution(y):
    n=1
    if y == 1:
        return 1
    while n**2 < y:
        n += 1
    if (n-1)**2+n > y: 
        return 2*n-2
    else:
        return 2*n-1

for x,y in arr:
    result.append(solution(y-x))
print(' '.join(list(map(str,result))))
