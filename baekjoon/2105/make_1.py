# 1로 만들기: 3으로 나눌 수 있으면 3으로 나누고, 2로 나눌 수 있으면 2로 나누고, 모두 안되면 1을 빼는 과정을 반복하여 총 연산 횟수를 출력하라.

n = int(input())
lst = [n+1 for _ in range(n+1)]
lst[1] = 0
for i in range(1,n+1):
    a,b,c = i+1, i*2, i*3
    if a <= n:
        lst[a] = min(lst[i]+1, lst[a])
    if b <= n:
        lst[b] = min(lst[i]+1, lst[b])
    if c <= n:
        lst[c] = min(lst[i]+1, lst[c])
print(lst[-1])