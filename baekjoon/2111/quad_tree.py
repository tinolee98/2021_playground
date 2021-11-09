N = int(input())
table = []
for _ in range(N):
    table.append(list(map(int,list(input()))))
#print(table)

def Check(table, r,c,size):
    std = table[r][c]
    if size == 1:
        return "{}".format(std)
    for cr in range(r,r+size):
        for cc in range(c,c+size):
            if table[cr][cc] != std:
                s = size//2
                return "("+Check(table, r,c,s) + Check(table,r,c+s,s) + Check(table,r+s,c,s) + Check(table,r+s,c+s,s) + ")"
    return "{}".format(std)
result = Check(table,0,0,N)
print(result)
