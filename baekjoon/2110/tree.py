from collections import deque
N = int(input())
tree = list(map(int, input().split()))
queue = deque()
queue.append(int(input()))

print(queue)

while queue:
    target = queue.popleft()
    if target >= N:
        break
    tree[target] = -2
    for i in range(N):
        if target == tree[i]:
            queue.append(i)
print(tree)

for i in range(N):
    if tree[i] == -1:
        queue.append(i)

result = 0
while queue:
    target = queue.popleft()
    if target not in tree:
        result += 1
    else:
        for i in range(N):
            if target == tree[i]:
                queue.append(i)
result = 0 if -1 not in tree else result
print(result)
    
