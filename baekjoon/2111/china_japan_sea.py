from collections import deque

heightsList = [[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]],[[2,1],[1,2]]]
outputs = [[[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]],[[0,0],[0,1],[1,0],[1,1]]]

def BFS(i,j,I,J,heights):
    dij = [(0,1),(0,-1), (1,0), (-1,0)]
    q = deque([(i,j)])
    visited = [[False for _ in range(J)] for _ in range(I)]
    visited[i][j] = True
    china = False
    japan = False
    while q:
        ti,tj = q.popleft()
        now = heights[ti][tj]
        if ti == 0 or tj == 0:
            china = True
        if ti == I-1 or tj == J-1:
            japan=True
        if china and japan:
            return [i,j]
        for di,dj in dij:
            ci = ti+di
            cj = tj+dj
            if 0<=ci<I and 0<=cj<J and not visited[ci][cj] and heights[ci][cj] <= now:
                q.append((ci,cj))
                visited[ci][cj] = True
    return False



for heights, output in zip(heightsList, outputs):
    print(heights, output)
    I = len(heights)
    J = len(heights[0])
    result = []
    for i in range(I):
        for j in range(J):
            temp = BFS(i,j,I,J, heights)
            if temp:
                result.append(temp)
    print(result)
    if result == output:
        print("success")
    else:
        print("fail")