# 셀프 넘버: 어떠한 수의 자기 자신과 각 자리 수의 합으로 이루어질 수 있는 수가 아닌 수들의 목록을 출력하라.

lst = list(range(10001))

for i in range(1,10000+1):
    s = i
    t = str(i)
    for j in range(len(t)):
        s += int(t[j])
    if s > 1 and s <= 10000:
        lst[s] = 0
cnt = 0
for i in range(1,10000+1):
    if lst[i] != 0:
        print(lst[i])