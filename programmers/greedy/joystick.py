# 조이스틱 문제: 영어 이름을 만들기 위해 'AAA' 와 같은 초기 모양에서 조이스틱을 이용해 알파벳을 바꾼다.
# 이때 위아래 방향으로는 알파벳을 바꾸고, 좌우방향으로는 커서의 위치를 바꿀 수 있을 때, 원하는 이름을 만들기 위해 필요한 조이스틱 최소 사용 횟수는?
def solution(name):
    goal = []
    result = []
    cnt = 0
    way = []
    for i in range(len(name)):
        if name[i] == 'A':
            way.append(1)
        else:
            way.append(0)
        result.append(1)
        goal.append(ord(name[i])-64)
    print(result,goal)
    # A : 1, Z : 26, 알파벳 바꾸는 경우만 체크
    for i in range(len(goal)):
        dif = abs(result[i]-goal[i])
        print(result[i],goal[i],dif)
        if dif >= 13:
            cnt += 26-dif
        else:
            cnt += dif
        print("here",cnt)

    # 커서를 이동하는 횟수 카운팅
    # j는 커서의 현 위치를 나타냄 (시작점)
    j=0
    print("cnt",cnt)
    # 1이 A 혹은 이미 바꾼 알파벳을 의미하므로 더이상 바꿀 문자가 없을 때까지 while 문 반복
    while 0 in way:
        print(way)
        # 현위치를 다녀갔음을 표시
        way[j] = 1
        # 좌(up), 우(down)로 1을 더하고 빼면서 커서를 양방향으로 움직이며 0이 저장되어 있는 가까운 거리의 index를 찾음
        # 이때 움직인 만큼 cnt에 1씩 더해주어 커서의 움직임을 카운팅
        up, down = j,j
        go = True
        while go:
            print("up or down", up, down)
            print("up",way[up],"down",way[down])
            up +=1
            down -= 1
            cnt +=1
            if up != j and (way[up] == 0 or way[down] == 0):
                go = False
        if way[up] == 0:
            way[up] = 1
            j = up
        elif way[down] == 0:
            way[down] = 1
            j = down
    print(cnt)
    return cnt

solution(list(map(str,input(">> ").split())))