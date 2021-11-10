from collections import deque
N,M = list(map(int, input().split()))
visited = [False for _ in range(101)]
ladder = [[],[]]
snake = [[],[]]

for _ in range(N):
    start, end = list(map(int, input().split()))
    ladder[0].append(start)
    ladder[1].append(end)
for _ in range(M):
    start, end = list(map(int, input().split()))
    snake[0].append(start)
    snake[1].append(end)

q = deque([1])

def CheckSnake(i,snake):
    return snake[1][snake[0].index(i)]

def CheckLadder(i,ladder):
    return ladder[1][ladder[0].index(i)]

def FindNext(q,ladder, snake, visited):
    nextLst = deque()
    while q:
        now = q.popleft()
        visited[now] = True
        for next in range(now+1, now+7):
            if next == 100:
                return deque()
            if 0<next<100 and not visited[next]:
                if next in ladder[0]:
                    temp = CheckLadder(next, ladder)
                    if temp and not visited[temp]:
                        visited[temp] = True
                        nextLst.append(temp)
                elif next in snake[0]:
                    temp = CheckSnake(next, snake)
                    if temp and not visited[temp]:
                        visited[temp] = True
                        nextLst.append(temp)
                else:
                    visited[next] = True
                    nextLst.append(next)
        #print("now", now,"nextLst",nextLst)
    return nextLst

move = 0
while q:
    q = FindNext(q,ladder, snake, visited)
    move += 1
    #print("while q", q)
    
print(move)


# dp로 풀다가 실패한 케이스 (뱀, 사다리에 가면 최소 거리를 판단할 것이 아닌 무조건 이동해야함을 고려하지 않았음.)
# from collections import deque
# N,M = list(map(int, input().split()))
# INF = 101
# move = [INF for _ in range(101)]
# move[0] = 0
# move[1] = 0
# ladder = [[],[]]
# snake = [[],[]]

# for _ in range(N):
#     start, end = list(map(int, input().split()))
#     ladder[0].append(start)
#     ladder[1].append(end)
# for _ in range(M):
#     start, end = list(map(int, input().split()))
#     snake[0].append(start)
#     snake[1].append(end)

# q = deque([i for i in range(2,101)])

# while q:
#     i = q.popleft()
#     move[i] = min(min(move[max(0,i-6):i])+1, move[i])
#     if i in ladder[0]:
#         target = ladder[1][ladder[0].index(i)]
#         if move[target] > move[i]:
#             move[target] = move[i]
#             q += [j for j in range(target,101)]
#     elif i in snake[0]:
#         target = snake[1][snake[0].index(i)]
#         if move[target] > move[i]:
#             move[target] = move[i]
#             q += [j for j in range(target,101)]
# print(move[100])