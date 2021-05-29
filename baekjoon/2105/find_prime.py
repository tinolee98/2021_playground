# 소수 찾기: 주어진 수 중 소수의 개수를 출력하라

n = int(input())
m = list(map(int, input().split()))

max_ = max(m)
lst = list(range(0,max_+1))
for i in range(2,max_+1):
    for j in range(2,i):
        if i%j == 0 and i != j :
            lst[i] = 0
            break
prime = []
for i in lst:
    if i > 1:
        prime.append(i)
cnt = 0
for i in m:
    if i in prime:
        cnt += 1
print(cnt)