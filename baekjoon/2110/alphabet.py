from copy import *
R,C = list(map(int,input().split()))

map = []
originalVisited = [[False]*C for _ in range(R)]
for _ in range(R):
    lst = list(input())
    map.append(lst)
#print(map)


dc = [1,0,-1,0]
dr = [0,-1,0,1]

c,r = 0,0
len = 0
maxLen = 0
def move(maxLen,len,r,c,past,visited):
    copyVisited = deepcopy(visited)
    copyPast = deepcopy(past)
    if map[r][c] not in copyPast and not copyVisited[r][c]:
        copyPast += [map[r][c]]
        copyVisited[r][c] = True    
        for i in range(4):
            cc = c + dc[i]
            cr = r + dr[i]
            if 0<=cc<C and 0<=cr<R and not copyVisited[cr][cc]:
                #print(r,c, cr, cc, past)
                #print(copyVisited)
                #print("---")
                maxLen = max(maxLen,move(maxLen,len+1,cr,cc,copyPast,copyVisited))
                #print(r,c, cr, cc, past, "fail")
                #print(copyVisited)
                #print("---")
        return maxLen
    return len
    # visited를 deep copy 해야하나?

result = move(maxLen,0,0,0,[],originalVisited)
print(result)