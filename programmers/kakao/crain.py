# 인형 뽑기: 인형 뽑기 기계에서 뽑은 인형 중 연속해서 같은 인형이 나오면 이 인형의 개수를 체크하고, 이 수를 리턴하는 문제.

def solution(board, moves):
    stack = []
    height = [0 for _ in range(len(board))]
    count = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != 0 and height[j] == 0:
                height[j] = len(board)-i
    #print("height", height)
    for m in moves:
        m -= 1
        #print("num", m+1)
        if height[m] != 0:
            for i in range(len(board)):
                if board[i][m] != 0:
                    stack.append(board[i][m])
                    board[i][m] = 0
                    break
            height[m] -= 1
        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            count += 2
        #print("board\n", board)
        #print("height", height)
        #print("stack", stack)
        #print("count", count)
    return count

lst = [[[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]]
answer = [4]
answer_sheet = []
for item in lst:
    answer_sheet.append(solution(item[0], item[1]))
if answer == answer_sheet:
    print("true")
else:
    print("false")