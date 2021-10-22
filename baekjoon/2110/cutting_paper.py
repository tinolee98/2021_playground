N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

count = [0,0]

def slice(I,J,size):
    std = paper[I][J]
    success = True
    for i in range(I,I+size):
        for j in range(J, J+size):
            if paper[i][j] != std:
                success = False
                break
        if not success:
            break
    if success:
        count[std] += 1
    else:
        size //= 2
        for i in range(2):
            for j in range(2):
                slice(I+i*size, J+j*size, size)
slice(0,0,N)
for c in count:
    print(c)
