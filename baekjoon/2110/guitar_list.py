N,S,M = list(map(int, input().split()))
volumes = list(map(int, input().split()))

dp = {}

def change(i, now):
    if (i,now) in dp:
        return dp[(i,now)]
    if i == N:
        return now
    if 0<=now+volumes[i]<=M:
        if 0<=now-volumes[i]<=M:
            dp[(i,now)] = max(change(i+1, now+volumes[i]), change(i+1, now-volumes[i]))
            return dp[(i,now)]
        else:
            dp[(i,now)] = change(i+1, now+volumes[i])
            return dp[(i,now)]
    elif 0<=now-volumes[i]<=M:
        dp[(i,now)] = change(i+1, now-volumes[i])
        return dp[(i,now)]
    else:
        return -1
print(change(0,S))

