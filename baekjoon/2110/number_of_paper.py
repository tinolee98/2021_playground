import sys
N = int(input())

input = sys.stdin.readline

paper = []

count = [0,0,0]

for _ in range(N):
    paper.append(list(map(int,input().rstrip().split())))

def Check(x,y,size):
    sta = paper[x][y]
    ok = True
    for cx in range(x,x+size):
        for cy in range(y,y+size):
            if sta != paper[cx][cy]:
                ok = False
                break
        if not ok:
            break
    if ok:
        count[sta+1] += 1
    else:
        size //= 3
        for i in range(3):
            for j in range(3):
                Check(x+size*i, y+size*j, size)

Check(0,0,N)
for c in count:
    print(c)

