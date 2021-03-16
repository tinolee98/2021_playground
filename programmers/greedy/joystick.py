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
    # 이동하는 방법에 대해서
    j = 0
    #while 0 in way:
     #   way[j] = 1
      #  for i in range(len(way)):
       #     if way[i] == 0 and abs(j-i) < 10:pass
    #for i in range(len(result)):
    #    result[i] = chr(result[i]+64)
    #print(result)
    print(cnt-1)
    
    answer = 0
    return answer