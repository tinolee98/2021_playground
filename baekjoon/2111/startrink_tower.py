N = int(input())
board = [[] for _ in range(N)]

for _ in range(5):
    line = list(input())
    for i in range(N):
        tempLine = line[i*4:i*4+3]
        board[i].append(tempLine)

std = [
    [[1],[1,4],[]],
    [[1,2,3,7],[0,1,2,3,4,5,6,7,8,9],[5,6]],
    [[1,7],[0,1,7],[]],
    [[1,3,4,5,7,9],[0,1,2,3,4,5,6,7,8,9],[2]],
    [[1,4,7],[1,4,7],[]]
]

answer = 0
for i,b in enumerate(board):
    # print(i,b)
    check = []
    for k in range(5):
        for j in range(3):
            if b[k][j] == '#':
                check += std[k][j]
    check = list(set(check))
    # print(check)
    countSuccess = 10-len(check)
    sumSuccess = 45-sum(check)
    if countSuccess == 0:
        print(-1)
        exit()
    answer += (sumSuccess/countSuccess) * 10**(N-i-1)
print(round(answer,5))