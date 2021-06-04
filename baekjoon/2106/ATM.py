# ATM: n명의 사람들이 인출을 위해 소모하는 시간을 입력받고, 각 사람들이 대기 및 인출에 소요되는 시간들의 합을 출력하라

n = int(input())
time = list(map(int, input().split()))
time.sort()
result = 0
for i in range(n,0,-1):
    result += time[-i] * i
print(result)