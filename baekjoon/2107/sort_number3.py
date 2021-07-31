# 수 정렬하기 3
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()
for i in range(n):
    print(arr[i])
