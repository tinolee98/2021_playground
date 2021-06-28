# 오름차순2

n = int(input())

lst = []
for _ in range(n):
    lst.append(int(input()))
lst = set(lst)
lst = list(lst)
lst = sorted(lst)
for i in lst:
    print(i)