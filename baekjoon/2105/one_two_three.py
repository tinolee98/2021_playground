# 1,2,3 더하기: 모든 수는 1,2,3의 합으로만 표현이 가능하다. n < 11일 때, n을 나타낼 수 있는 경우의 수를 출력하라.

n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))
