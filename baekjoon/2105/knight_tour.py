# 나이트 투어: 나이트가 주어진 경로로 이동하여 다시 시작점으로 도착할 수 있는가?
dx = [-2,-1,1,2,2,1,-1,-2]
dy = [1,2,2,1,-1,-2,-2,-1]
ways = [input() for _ in range(36)]
visited = [[False]*6 for _ in range(6)]
nowX, nowY = ord(ways[0][0])-64, int(ways[0][1])
visited[nowX-1][nowY-1] = True
isValid = True
for i in range(1,36):
    curX, curY = ord(ways[i][0])-64, int(ways[i][1])
    if abs((nowX - curX)*(nowY - curY)) != 2:
        isValid = False
        break
    if visited[curX-1][curY-1]:
        isValid = False
        break
    visited[curX-1][curY-1] = True
    nowX, nowY = curX, curY
for way in visited:
    if False in way:
        isValid = False
for i in range(8):
    nx = nowX + dx[i]
    ny = nowY + dy[i]
    if nx != ord(ways[0][0])-64 or ny != int(ways[0][1]):
        isValid = False
    else:
        isValid = True
        break
if len(ways) != 36:
    isValid = False
if isValid:
    print("Valid")
else:
    print("Invalid")