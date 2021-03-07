# 백준 실버. 주어진 약수를 통해 원수 찾기
length = int(input())
lst= list(map(int,input().split()))
lst.sort()
result = lst[0]*lst[-1]
print(result)