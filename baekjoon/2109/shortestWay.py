import heapq

v,e = list(map(int, input().split()))
k = int(input())
table = [[] for _ in range(v+1)]
for _ in range(e):
    s,e,l = list(map(int, input().split()))
    table[s].append((e,l))
    #if (s,l) not in table[e]:
    #    table[e].append((e,s,l))
#print(table)

INF = int(1e7)

way = [INF for _ in range(v+1)]
way[k], way[0] = 0,0
visited = [False for _ in range(v+1)]
visited[k] = True
q = []
heapq.heappush(q,(0,k))
#print(way)
while q:
    dist, now = heapq.heappop(q)
    if way[now] < dist:
        continue
    for i in table[now]:
        cost = dist + i[1]
        if cost < way[i[0]]:
            way[i[0]] = cost
            heapq.heappush(q,(cost,i[0]))
    # print(dist, now)
    # print(table)
    # print(q)
    # print(way)
    # print("--------------")

result = list(way)
result = list(map(str,result[1:]))
for i in range(len(result)):
    if result[i] == "10000000":
        result[i] = "INF"    
print(' '.join(result))
