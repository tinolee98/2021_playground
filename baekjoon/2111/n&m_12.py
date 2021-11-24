N,M = list(map(int, input().split()))
nums = list(set(list(map(int, input().split()))))
nums.sort()
answer = []
visited = [0 for _ in range(10001)]
made = []
for n in nums:
    visited[n] += 1
def Func(size, result,last):
    if size == 0:
        num = ' '.join(list(map(str, result)))
        if num not in made:
            made.append(num)
            print(num)
    else:
        for n in nums:
            if last <= n:
                result.append(n)
                Func(size-1, result,n)
                result.pop()
Func(M,[],0)