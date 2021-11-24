N = int(input())
def Check(r,place):
    cnt = 0
    ok = True
    if r == N:
        return 1
    for c in range(N):
        ok = True
        for qr,qc in place:
            if c == qc or abs(r-qr) == abs(c-qc):
                ok = False
                break
        if ok:
            place.append((r,c))
            cnt += Check(r+1,place)
            place.pop()
    return cnt

print(Check(0,[]))