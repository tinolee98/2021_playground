# t: 계산하고자 하는 case의 개수
t = int(input())

# table: 입력받은 알고리즘랩스까지의 지도
# size: 각 지도의 크기에 대한 tuple
# table, size에 대한 정보를 수집하는 단계
table = [[] for _ in range(t)]
size = [(0,0) for _ in range(t)]
for i in range(t):
    size[i] = tuple(map(int, input().split()))
    for n in range(size[i][0]):
        table[i].append(list(map(int,input().split())))

# 움직일 수 있는 경로는 오른쪽, 아래쪽 방향밖에 존재하지 않기 때문에 pascal's triangle에서 영감을 받아서 함수 제작 (각 위치는 바로 위, 왼쪽의 값에 영향을 받음.)
# n,m: size에서 각 지도의 크기를 불러옴.
# way: 각 좌표까지 가는 길에 대한 경로 리스트
# ex) 1번 case way[1][1] = [[1,3,19], [1,17,19]] <- 1번 지도에서 (1,1) 좌표로 이동할 수 있는 각 경로의 정보
# distance: way 리스트에서 경로의 거리 합에 대한 리스트
# ex) 1번 case distance[1][1] = [23, 37] <- 1번 지도에서 (1,1) 좌표로 이동할 수 있는 각 경로의 길이
# pt: 각 좌표까지 가는 길의 수
# ex) 1번 case pt[1][1] = 2 <- 1번 지도에서 (1,1) 좌표로 이동할 수 있는 경로의 수

def pascal(i,graph):
    n,m = size[i]
    way = [[[] for _ in range(m)] for _ in range(n)]
    distance = [[[] for _ in range(m)] for _ in range(n)]
    pt = [[0]*m for _ in range(n)]

    # 앞서 말했듯이 pascal's triangle처럼 아래, 우 방향으로만 이동하므로 for 문 2개를 이용하면 구현 가능.
    for j in range(n):
        for k in range(m):
            now = graph[j][k]

            # (0,0)
            if j == 0 and k == 0:
                way[j][k].append([now])
                distance[j][k].append(now)
                pt[j][k] = 1

            # (0,k): 가장 윗줄 (오른쪽으로만 이동할 수 있는 경우)
            # (0,k-1)에서 (0,k)로 이동할 수 있는 경우, way[0][k]에 way[0][k-1]의 각 경로에 now를 추가하여 update
            # 또한 각 경로의 길이와 개수도 update
            elif j == 0:
                if len(way[j][k-1]) > 0 and now not in way[j][k-1][0]:
                    tempList = way[j][k-1][0] + [now]
                    way[j][k].append(tempList)
                    distance[j][k].append(distance[j][k-1][0] + now)
                    pt[j][k] = 1
            
            # (j,0): 가장 왼쪽 줄 (아래로만 이동할 수 있는 경우) (0,k)와 동일한 방법
            elif k == 0:
                if len(way[j-1][k]) > 0 and now not in way[j-1][k][0]:
                    tempList = way[j-1][k][0] + [now]
                    way[j][k].append(tempList)
                    distance[j][k].append(distance[j-1][k][0] + now)
                    pt[j][k] = 1
            
            # (j,k): 오른쪽, 아래쪽 모두 이동할 수 있는 경우
            # 방법은 위의 방법과 같고, 왼쪽 값에 영향을 받는 경우와 위쪽 값에 영향을 받는 경우를 나누어서 계산
            else:
                for e, w in enumerate(way[j][k-1]):
                    if now not in w:
                        tempList = w + [now]
                        way[j][k].append(tempList)
                        distance[j][k].append(distance[j][k-1][e] + now)
                        pt[j][k] += 1
                
                for e, w in enumerate(way[j-1][k]):
                    if now not in w:
                        tempList = w + [now]
                        way[j][k].append(tempList)
                        distance[j][k].append(distance[j-1][k][e] + now)
                        pt[j][k] += 1
    
    # endpoint까지 갈 수 없는 경우, 도착할 수 있는 경우의 수는 0, 최대 길이는 -1을 return
    if len(distance[n-1][m-1]) == 0:
        return 0, -1
    
    # 도착할 수 있는 경우의 수는 마지막 좌표의 pt, 최대 길이는 마지막 좌표의 distance 내의 최대값
    return pt[n-1][m-1], max(distance[n-1][m-1])

for i,graph in enumerate(table):
    numberOfWays, maxDistance= pascal(i,graph)
    print()
    print("In {} case,".format(i+1))
    print("The number of ways to endpoint is {} and maximum of distance is {}".format(numberOfWays, maxDistance))
