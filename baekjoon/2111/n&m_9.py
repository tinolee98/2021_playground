N,M = list(map(int, input().split()))
nums = list(map(int, input().split()))
nums.sort()
answer = []
visited = [0 for _ in range(10001)]
made = []
for n in nums:
    visited[n] += 1
def Func(size, result,visited):
    if size == 0:
        num = ' '.join(list(map(str, result)))
        if num not in made:
            made.append(num)
            print(num)
    else:
        for n in nums:
            if visited[n]:
                result.append(n)
                visited[n] -= 1
                Func(size-1, result,visited)
                visited[n] += 1
                result.pop()
Func(M,[],visited)