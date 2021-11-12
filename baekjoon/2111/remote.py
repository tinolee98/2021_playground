N = input()
M = int(input())
btn = [i for i in range(10)]
if M > 0:
    broken = list(map(int, input().split()))
    for n in broken:
        btn.remove(n)
#print(btn)
start = 100
down, now, up = '','',''
a,b = '',''
same = True
tempDown = '0'
tempUp ='0'
if M == 10:
    print(abs(int(N)-100))
    exit()
for n in N:
    n = int(n)
    if n in btn:
        down = now
        up = now
        now += str(n)
        for i in range(len(btn)):
            if btn[i] < n:
                tempDown = btn[i]
            elif btn[i] > n:
                tempUp = btn[i]
                break
        down += str(tempDown)
        up += str(tempUp)
    else:
        # print(down,now, up)
        tempDown = int(down+ str(btn[-1])*(len(N)-len(down)))
        tempUp = int(up+str(btn[0])*(len(N)-len(up)))
        nowDown = int(now + str(btn[0])*(len(N)-len(now)))
        nowUp = int(now + str(btn[-1])*(len(N)-len(now)))
        target = int(N)
        # print("temp", tempDown, nowDown, nowUp, tempUp)
        if tempDown<target<nowDown:
            a = tempDown
            b = nowDown
        elif nowDown<target<nowUp:
            for i in range(len(btn)):
                if btn[i] < n:
                    tempDown = btn[i]
                elif btn[i] > n:
                    tempUp = btn[i]
                    break
            a = now + str(tempDown) + str(btn[-1])*(len(N)-len(now)-1)
            b = now + str(tempUp) + str(btn[0])*(len(N)-len(now)-1)
        else:
            a = nowUp
            b = tempUp
        same = False
        break
    # print(down, now, up)
minimum =int(str(btn[-1])*(len(N)-1)) if len(N)-1 >0 else -1
if btn[0] == 0 and len(btn) > 1:
    maximum = int(str(btn[1])+'0'*(len(N)))
else:
    maximum = int(str(btn[0])*(len(N)+1))
result = []
if not same:
    # print("not same",minimum,a,b,maximum,100)
    lst = [int(a),int(b),maximum,100]
    if minimum != -1:
        lst.append(minimum)
    for n in lst:
        if n != 100:
            result.append(abs(int(N)-n)+len(str(n)))
        else:
            result.append(abs(int(N)-n))
else:
    # print("same",minimum, down, now, up, maximum,100)
    lst = [int(down),int(now),int(up),maximum,100]
    if minimum != -1:
        lst.append(minimum)
    for n in lst:
        if n != 100:
            result.append(abs(int(N)-n)+len(str(n)))
        else:
            result.append(abs(int(N)-n))
print(min(result))