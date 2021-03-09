#8*8크기의 체스판에 왕이 하나 있다. 킹의 현재 위치가 주어진다. 체스판에서 말의 위치는 다음과 같이 주어진다. 알파벳 하나와 숫자 하나로 이루어져 있는데, 알파벳은 열을 상징하고, 숫자는 행을 상징한다. 열은 가장 왼쪽 열이 A이고, 가장 오른쪽 열이 H까지 이고, 행은 가장 아래가 1이고 가장 위가 8이다. 예를 들어, 왼쪽 아래 코너는 A1이고, 그 오른쪽 칸은 B1이다.

#킹은 다음과 같이 움직일 수 있다.

#R : 한 칸 오른쪽으로
#L : 한 칸 왼쪽으로
#B : 한 칸 아래로
#T : 한 칸 위로
#RT : 오른쪽 위 대각선으로
#LT : 왼쪽 위 대각선으로
#RB : 오른쪽 아래 대각선으로
#LB : 왼쪽 아래 대각선으로
#체스판에는 돌이 하나 있는데, 돌과 같은 곳으로 이동할 때는, 돌을 킹이 움직인 방향과 같은 방향으로 한 칸 이동시킨다. 아래 그림을 참고하자.

#입력으로 킹이 어떻게 움직여야 하는지 주어진다. 입력으로 주어진 대로 움직여서 킹이나 돌이 체스판 밖으로 나갈 경우에는 그 이동은 건너 뛰고 다음 이동을 한다.

#킹과 돌의 마지막 위치를 구하는 프로그램을 작성하시오.
king, stone, move = input().split()
move = int(move)
king = list(king)
king[1] = int(king[1])
stone = list(stone)
stone[1] = int(stone[1])
#print(move, king, stone)
columns = ['A','B','C','D','E','F','G','H']
rows = [1,2,3,4,5,6,7,8]
dx = [1,-1,0,0,1,-1,1,-1]   # R,L,B,T,RT,LT,RB,LB 순
dy = [0,0,-1,1,1,1,-1,-1]
direction = ['R','L','B','T','RT','LT','RB','LB']
way = []
for i in range(move):
    way.append(input())

for moving in way:
    index = direction.index(moving) # 움직일 방향을 정하는 단계 ex) B가 입력되었다면 index = 2 이다.
    kx,ky = chr(ord(king[0]) + dx[index]), king[1] + dy[index]    # king이 이동할 위치
    #print(kx,ky)
    if kx in columns and ky in rows:            # king이 이동한 좌표가 체스판 위에 존재한다면
        if kx == stone[0] and ky == stone[1]:   # 이동한 위치가 돌이 있는 곳이라면
            sx, sy = chr(ord(stone[0]) + dx[index]), stone[1] + dy[index] # 돌의 위치를 구하여 돌이 움직일 수 있는지 확인 후, 이동 혹은 정지
            if sx in columns and sy in rows:
                king = [kx,ky]
                stone = [sx,sy]
            else:
                continue
        else:
            king = [kx,ky]
    #print("king: ",king)   # king과 돌의 위치 확인하기
    #print("stone: ",stone)
king[1] = str(king[1])
stone[1] = str(stone[1])
print(''.join(king))
print(''.join(stone))