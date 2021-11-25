import heapq
now, brother = list(map(int, input().split()))
INF = 100001
dp = [INF]*INF
visited = [False]*INF
q = []
while now < INF:
    q.append((0,now))
    if now == 0:
        break
    now *= 2
while q:
    time, now = heapq.heappop(q)
    # print(time, now)
    if now == brother:
        print(time)
        break
    if not visited[now]:
        visited[now] = True
        next = 2*now
        for next in [now-1, now+1]:
            if 0<=next<INF and not visited[next]:
                heapq.heappush(q,(time+1, next))
                while next < INF:
                    if next == 0 or visited[next]:
                        break
                    heapq.heappush(q,(time+1,next))
                    next *= 2
    # print(q)
        

# from collections import deque
# subin, brother = list(map(int, input().split()))
# INF = 200001
# dp = [INF]*INF
# dp[subin] = 0
# visited = [False]*INF
# q = deque([subin])
# visited[subin] = True
# next = subin
# while next < INF:
#     if next == 0:
#         break
#     q.append(next)
#     dp[next] = 0
#     next *= 2
# # print(q)
# while q:
#     now = q.popleft()
#     # if now == brother:
#     #     break
#     for next in [now-1, now+1]:
#         if 0<=next<INF and not visited[next]:
#             visited[next] = True
#             dp[next] = min(dp[next], dp[now]+1)
#             q.append(next)
#             temp = 2*next
#             while temp < INF:
#                 if temp == 0 or visited[temp]:
#                     break
#                 q.appendleft(temp)
#                 dp[temp] = min(dp[temp], dp[now]+1)
#                 visited[temp] = True
#     # print("q",q)
# print(dp[brother])