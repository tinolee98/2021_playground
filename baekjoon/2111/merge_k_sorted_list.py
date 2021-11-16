# This problem is not in Baekjoon.
lists = [[1,4,5],[1,3,4],[2,6]]
output = [1,1,2,3,4,4,5,6]
result = []
indices = [0 for _ in range(len(lists))]
l = 0
for lst in lists:
    l += len(lst)

for i in range(l):
    minimum = 10001
    index = -1
    for j in range(len(lists)):
        if indices[j] < len(lists[j]):
            now = lists[j][indices[j]]
            if minimum > now:
                minimum = now
                index = j
    result.append(minimum)
    indices[index] += 1
    print(indices)
print(result)

if output == result:
    print("success")
else:
    print("fail", result)