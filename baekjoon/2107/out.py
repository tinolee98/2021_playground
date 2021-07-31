# 퇴사하기
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
print(arr)

pay = [0] * (n+1)
print(pay)
for i in range(n):
    day = arr[i][0] + i
    print(day, i)
    if day <= n:
        pay[day] = max(arr[i][1] + max(pay[:i+1]), pay[day])
        print(pay[day])
    else:
        print("pass")
    
    print(pay)
print(max(pay))