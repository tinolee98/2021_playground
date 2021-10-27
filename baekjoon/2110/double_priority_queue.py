import sys

def deleteMin(n,minQ):
    #print("deleteMin")
    parent = minQ.index(n)
    exist = True
    if len(minQ) > 1:
        maximum = minQ.pop()
    else:
        exist = False
    if parent >= len(minQ):
        return
    ok = True if exist else False
    while ok:
        onlyLeft = False
        if parent*2 >= len(minQ):
            break
        elif parent*2+1 >= len(minQ):
            onlyLeft = True
        else:
            ri = parent*2+1
            rv = minQ[ri]
        li = parent*2
        lv = minQ[li]
        if (onlyLeft or (not onlyLeft and lv <= rv )) and lv < maximum:
            minQ[parent] = lv
            parent = li
        elif (not onlyLeft and rv < lv) and rv < maximum:
            minQ[parent] = rv
            parent = ri
        else:
            ok = False
    if len(minQ) > 1:
        minQ[parent] = maximum

def deleteMax(n,maxQ):
    #print("deleteMax")
    exist = True
    parent = maxQ.index(n)
    if len(maxQ) > 1:
        minimum = maxQ.pop()
    else:
        exist = False
    if parent >= len(maxQ):
        return
    ok = True if exist else False
    while ok:
        onlyLeft = False
        if parent*2 >= len(maxQ):
            break
        elif parent*2+1 >= len(maxQ):
            onlyLeft = True
        else:
            ri = parent*2+1
            rv = maxQ[ri]
        li = parent*2
        lv = maxQ[li]
        if (onlyLeft or (not onlyLeft and lv >= rv )) and lv > minimum:
            maxQ[parent] = lv
            parent = li
        elif (not onlyLeft and rv < lv) and rv > minimum:
            maxQ[parent] = rv
            parent = ri
        else:
            ok = False
    if len(maxQ) > 1:
        maxQ[parent] = minimum

def delete(n,minQ, maxQ):
    #print("delete")
    if len(minQ) == 1:
        return 
    if n == -1:
        # minQ
        exist = True
        if len(minQ) > 1:
            now = minQ[1]
            maximum = minQ.pop()
        else:
            exist = False
        parent = 1
        ok = True if exist else False
        while ok:
            onlyLeft = False
            if parent*2 >= len(minQ):
                break
            elif parent*2+1 >= len(minQ):
                onlyLeft = True
            else:
                ri = parent*2+1
                rv = minQ[ri]
            li = parent*2
            lv = minQ[li]
            if (onlyLeft or (not onlyLeft and lv <= rv )) and lv < maximum:
                minQ[parent] = lv
                parent = li
            elif (not onlyLeft and rv < lv) and rv < maximum:
                minQ[parent] = rv
                parent = ri
            else:
                ok = False
        if len(minQ) > 1:
            minQ[parent] = maximum
        deleteMax(now,maxQ)
    else:
        # maxQ
        exist = True
        if len(maxQ) > 1:
            now = maxQ[1]
            minimum = maxQ.pop()
        parent = 1
        ok = True if exist else False
        while ok:
            onlyLeft = False
            if parent*2 >= len(maxQ):
                break
            elif parent*2+1 >= len(maxQ):
                onlyLeft = True
            else:
                ri = parent*2+1
                rv = maxQ[ri]
            li = parent*2
            lv = maxQ[li]
            if (onlyLeft or (not onlyLeft and lv >= rv )) and lv > minimum:
                maxQ[parent] = lv
                parent = li
            elif (not onlyLeft and rv < lv) and rv > minimum:
                maxQ[parent] = rv
                parent = ri
            else:
                ok = False
        if len(maxQ) > 1:
            maxQ[parent] = minimum
        deleteMin(now,minQ)
    
    
    
    

def insert(n,minQ, maxQ):
    #print("insert")
    minQ.append(n)
    maxQ.append(n)
    child = len(minQ)-1
    while child > 1:
        parent = child // 2
        if minQ[child] < minQ[parent]:
            minQ[child], minQ[parent] = minQ[parent], minQ[child]
            child = parent
        else:
            break
    child = len(maxQ)-1
    while child > 1:
        parent = child // 2
        if maxQ[child] > maxQ[parent]:
            maxQ[child], maxQ[parent] = maxQ[parent], maxQ[child]
            child = parent
        else:
            break
N = int(input())
cmds = [[] for _ in range(N)]
input = sys.stdin.readline
for i in range(N):
    M = int(input().rstrip())
    minQ = [0]
    maxQ = [0]
    for j in range(M):
        c,n = list(input().rstrip().split())
        n=int(n)
        if c == "I":
            insert(n,minQ, maxQ)
            #print("minQ", minQ)
            #print("maxQ", maxQ)
        else:
            delete(n,minQ, maxQ)
            #print("minQ delete", minQ)
            #print("maxQ delete", maxQ)
    if len(minQ) == 1:
        print("EMPTY")
    else:
        print(maxQ[1],minQ[1])