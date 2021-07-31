# 1,2,3의 합으로 수를 나타내는 방법의 수

t = int(input())

lst = []

for _ in range(t):
    lst.append(int(input()))

arr = [0] * (max(lst)+1)
arr[1] = 1
arr[2] = 2
arr[3] = 4
for i in range(4,max(lst)+1):
    arr[i] = arr[i-3] + arr[i-2] + arr[i-1]
for i in lst:
    print(arr[i])