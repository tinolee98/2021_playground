# new 행렬 회전
# 행렬 회전시키기: rows*columns 사이즈의 행렬을 주어진 query에 해당하는 부분 행렬의 테두리를 회전시키려고 한다.
# 그리고 회전시킨 테두리 중 가장 작은 값들을 리스트에 담아 리턴하자.

def solution(rows, columns, queries):
    answer = []
    graph = [[j*columns+i+1 for i in range(columns)] for j in range(rows)]
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    #print(graph)
    for a,b,c,d in queries:
        direction = 0
        endpoints = [(b-1, a-1), (b-1, c-1), (d-1, a-1), (d-1, c-1)]
        (x,y) = endpoints[0]
        Range = []
        while True:
            if direction > 3:
                break
            X = x+dx[direction]
            Y = y+dy[direction]
            if (X,Y) in endpoints:
                direction += 1
            Range.append((X,Y))
            x,y = X,Y
        num = graph[a-1][b-1]
        minimum = 10001
        for x,y in Range:
            temp = graph[y][x]
            graph[y][x],num = num, temp
            minimum = min(minimum, num)
        answer.append(minimum)
        
    return answer

lst = [[6,6,[[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]]]
answer_sheet = []
for item in lst:
    answer_sheet.append(solution(item[0], item[1], item[2]))

answer = [[8, 10, 25]]
if answer_sheet == answer:
    print("true")
else:
    print("false")