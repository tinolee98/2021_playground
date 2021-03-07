# 백준 실버. 좋은 구간
# 정수 집합 S가 주어졌을때, 다음 조건을 만족하는 구간 [A, B]를 좋은 구간이라고 한다.
# 1. A와 B는 양의 정수이고, A < B를 만족한다.
# 2. A ≤ x ≤ B를 만족하는 모든 정수 x가 집합 S에 속하지 않는다.
# 집합 S와 n이 주어졌을 때, n을 포함하는 좋은 구간의 개수를 구해보자.
L = int(input())
S = list(map(int,input().split()))
n = int(input())
S.sort()
for i in range(len(S)):
    if S[0] >= n:
        a,b = 1,S[0]
        break
    if S[i] <= n and S[i+1] > n:
        a,b = S[i], S[i+1]
        break
count = (n-a)*(b-n) - 1 # a=1, n=2, b=3 일때, [1,2]로 경우의 수가 한 가지 존재하는데 이를 못찾아냄. (n<b 인 경우?)
if count < 0:
    print(0)
else:
    print(count)