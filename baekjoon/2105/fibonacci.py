# 피보나치 수열: 피보나치 수열을 구하는 과정에서 f(0)과 f(1)이 호출 되는 횟수를 출력
def fibonacci(n):
    if n == 0:
        memo[n] = 0
    elif n == 1:
        memo[n] = 1
    else:
        memo[n] = memo[n-1] + memo[n-2]

t = int(input())
lst = []
result = []
memo = {}
for i in range(40):
    fibonacci(i)
for i in range(t):
    lst.append(int(input()))
for i in lst:
    if i == 0:
        print("1 0")
    else:
        print("{} {}".format(memo[i-1],memo[i]))

'''for i in range(t):
    lst.append(int(input()))
for i in lst:
    fibonacci(i)
    a,b = result.count(0), result.count(1)
    print('{} {} {}'.format(i,a,b))
    result = []'''

# 1 0 1 1 2 3 5 8 13 21 34
# ' 0 1 2 3 4 5 6 7  8  9