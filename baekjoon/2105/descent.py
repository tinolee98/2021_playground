# 내림차순 정렬
n = str(input())
lst = list(map(str, n))
lst.sort(reverse=True)
print(''.join(lst))