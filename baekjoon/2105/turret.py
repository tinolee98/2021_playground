# 터렛: 두 좌표에서 특정 거리만큼 떨어져있는 지점은 몇개 존재하는가?
n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int,input().split())))
for x1, y1, r1, x2, y2, r2 in lst:
    distance = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
    pr = r1+r2
    mr = max(r1,r2) - min(r1,r2)
    #print(distance, pr, mr)
    if pr == distance or mr == distance and distance != 0:
        print(1)
    elif distance == 0 and mr == 0:
        print(-1)
    elif distance != 0 and distance > mr and distance < pr:
        print(2)
    elif (distance == 0 and mr != 0) or (distance != 0 and mr == 0):
        print(0)
    else:
        print(0)
