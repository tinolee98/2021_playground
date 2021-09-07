# 네트워크: 서로 연결되어있는 컴퓨터들을 하나의 네트워크라고 볼 수 있을 때, 네트워크의 수를 리턴하자.

from collections import deque

def BFS(check, i, nodes):
    queue = deque()
    for j in range(len(nodes)):
        if nodes[i][j] == 1:
            queue.append(i)    
    while (queue):
        m = queue.popleft()
        if m not in check:
            check.append(m)
            for j in range(len(nodes)):
                if nodes[m][j] == 1:
                    queue.append(j)
        queue = deque(set(queue))

def solution(n, computers):
    answer = 0
    check = []
    for i in range(n):
        if i not in check:
            BFS(check, i, computers)
            answer += 1
    return answer

lst = [[3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]], [3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]]]
answer_sheet = []
for item in lst:
    answer_sheet.append(solution(item[0], item[1]))

answer = [2,1]
if answer_sheet == answer:
    print("true")
else:
    print("false")