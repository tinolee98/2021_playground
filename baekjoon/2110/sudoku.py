from copy import deepcopy
sudoku = []
for _ in range(9):
    lst = list(map(int,input().split()))
    sudoku.append(lst)

numInRow = [[1,2,3,4,5,6,7,8,9] for _ in range(9)]
numInColumn = [[1,2,3,4,5,6,7,8,9]for _ in range(9)]
numInBox = [[1,2,3,4,5,6,7,8,9]for _ in range(9)]

def findBox(i,j):
    if 0<=i<3:
        if 0<=j<3:
            return 0
        elif 3<=j<6:
            return 1
        else:
            return 2
    elif 3<=i<6:
        if 0<=j<3:
            return 3
        elif 3<=j<6:
            return 4
        else:
            return 5
    else:
        if 0<=j<3:
            return 6
        elif 3<=j<6:
            return 7
        else:
            return 8

def removeNum(n,i,j):
    numInRow[i].remove(n)
    numInColumn[j].remove(n)
    boxIndex = findBox(i,j)
    numInBox[boxIndex].remove(n)




q = []
tempDict = {}

for i in range(9):
    for j in range(9):
        if sudoku[i][j] != 0:
            n = sudoku[i][j]
            removeNum(n,i,j)
        else:
            q.append((i,j))

#print(numInRow)
#print(numInColumn)
#print(numInBox)
#print(q)

resultStack = deepcopy(q)
stop = len(resultStack)
i,j = q.pop()
def numCheck(i,j,stop):
    print("i, j:", i,j)
    print(tempDict)
    print(resultStack)
    ok = True
    if stop == 0:
        print("stop!")
        for x,y in resultStack:
            sudoku[y][x] = tempDict[(x,y)]
        print(sudoku)
        exit()
    for n in numInRow[i]:
        if n in numInColumn[j] and n in numInBox[findBox(i,j)]:
            tempDict[(i,j)] = n
            if len(q) > 0 and ok:
                ci,cj = q.pop()
                print("c",ci,cj)
                numCheck(ci,cj,stop-1)
            else:
                return
        # else:
        #     print("append", i,j)
        #     q.append((i,j))
numCheck(i,j,stop)
    
for lst in sudoku:
    print(' '.join(list(map(str,lst))))