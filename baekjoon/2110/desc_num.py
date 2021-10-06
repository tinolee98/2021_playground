N = int(input())

table = []
table.append([1 for i in range(10)])
#print(table)
total = 9
lst = []
n = 1
m = 0
if N >= 1023:
    print(-1)
    exit()
# elif N == 0:
#     print(0)
#     exit()
while N > total:
    temp = 0
    if m == 10:
        m = 0
        n += 1
        continue
    if len(table) < n+1:
        table.append([])
    if m >= n:
        for i in range(m):
            temp += table[n-1][i]
    #print(temp)
    table[n].append(temp)
    m += 1
    total += temp
#print(table)

m -= 1

def f(n,m,total):
    #print("---")
    #print("n: {} m: {}".format(n,m))
    #print("total: {} N: {}".format(total, N))
    now = table[n][m]
    if total == N:
        temp = 0
        for _ in range(n+1):
            temp = temp*10 + m
            m -= 1
        return str(temp)

    if total-now < N:
        return str(m) + f(n-1,m-1,total)
    else:
        return f(n,m-1,total-now)
    
if N > 10:
    result = f(n,m,total)
else:
    result = str(N)
print(result)
