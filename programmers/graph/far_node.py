from collections import deque
def solution(n, edge):
    dist = [50001] * (n+1)
    dist[0], dist[1] = 0,0
    edge.sort()
    visited = [False]*(n+1)
    visited[0],visited[1] = True, True
    way = [[] for i in range(n+1)] 
    for lst in edge:
        way[lst[0]] += [lst[1]]
        way[lst[1]] += [lst[0]]
    print(way)
    queue = deque()
    queue.append(1)
    while queue:
        i = queue.popleft()
        for j in way[i]:
            if not visited[j]:
                visited[j] = True
                queue.append(j)
                dist[j] = min(dist[i]+1, dist[j])
    print(dist)
    maximum = max(dist)
    cnt = 0
    for i in dist:
        if maximum == i:
            cnt+=1
    return cnt

solution(6,[[3,6],[4,3],[3,2],[1,3],[1,2],[2,4],[5,2]])