N,K = list(map(int, input().split()))

def Function():
    b = bin(N)
    if N == K or b.count('1') <= K:
        return 0
    elif N < K:
        return -1
    else:         
        count = 0
        for i in range(len(b)):
            if b[i]== '1':
                count += 1
            if count == K:
                b = b[i:]
                break
        # print(b)
        std = 2**(len(b))
        b = "0b"+b
        b = int(b,2)
        # print(std)
        # print(b)
        return std-b

print(Function())
#print(format(N,'b'))