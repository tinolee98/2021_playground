# 백준 실버 문제. 다리 놓기: 강을 중심으로 좌측엔 N개, 우측엔 M개의 포인트가 있다 (N<=M). 다리를 놓는 경우의 수를 구하시오.
case = int(input())
lst = []
for i in range(case):
    lst.append(map(int,input().split()))
for i,j in lst:
    result = 1
    if j <= 2*i:
        for k in range(i+1,j+1):
            result *= k
        for k in range(1,j-i+1):
            result /= k
    else:
        for k in range(j-i+1,j+1):
            result *= k
        for k in range(1,i+1):
            result /= k
    print(int(result))