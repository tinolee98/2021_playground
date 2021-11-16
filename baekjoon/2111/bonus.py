# This problem is not in Baekjoon.
from collections import deque

evaluations = [[1,0,2], [12,4,3,11,34,34,1,67]]
outputs = [5000, 16000]

def BFS(i,m,lst,result):
    left = lst[i-1] if 0<=i-1 else m+1
    right = lst[i+1] if i+1<len(lst) else m+1
    if lst[i]<left and lst[i]<right:
        q = deque([(i-1,i+1)])
        visited = [False for _ in range(len(lst))]
        visited[i] = True
        result[i] = 1000
        ev = 1000
        while q:
            left,right = q.popleft()
            ev += 1000
            if 0<=left<len(lst):
                result[left] = min(ev, result[left])
            if 0<=right<len(lst):
                result[right] = min(ev, result[right])
            if 0<=left<len(lst) or 0<=right<len(lst):
                q.append((left-1, right+1))

for evaluation, output in zip(evaluations, outputs):
    maximum = max(evaluation)
    result = [1000*len(evaluation)+1 for _ in range(len(evaluation))]
    for i in range(len(evaluation)):
        BFS(i,maximum,evaluation, result)
    print(sum(result))