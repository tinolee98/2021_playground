sudoku = []
for _ in range(9):
    sudoku.append(list(map(int, input().split())))
print(sudoku)

stack = []

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            stack.append((i,j))

index = len(stack)

def checkRow(n,i):
    if n in sudoku[i]:
        return False
    else:
        return True

def checkColumn(n,j):
    for a in range(9):
        if n == sudoku[a][j]:
            return False
    return True

def checkBox(n,i,j):
    I = (i//3)*3
    J = (j//3)*3
    for y in range(I,I+3):
        for x in range(J,J+3):
            if n == sudoku[y][x]:
                return False
    return True

def isOk(n,i,j):
    print("isOk")
    checkBox(1,2,3)

isOk(1,2,3)