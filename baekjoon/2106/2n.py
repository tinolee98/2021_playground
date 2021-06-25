# 2xn 크기의 직사각형을 1x2, 2x1 타일로 채우는 방법의 수

n = int(input())

lst = [0] * (n+1)
lst[0] = 1
lst[1] = 1
for i in range(2,n+1):
    lst[i] += lst[i-1] + lst[i-2]
print(lst[-1]%10007)