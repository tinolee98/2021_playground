import sys
N = int(input())
input = sys.stdin.readline
sch = []

for _ in range(N):
    sch.append(tuple(map(int, input().rstrip().split())))
sch = sorted(sch, key=lambda s: s[1])
temp = []
tempEnd = sch[0][1]
finalSch = []
for t in sch:  
    if t[1] == tempEnd:
        temp.append(t)
    else:
        temp = sorted(temp, key= lambda s: s[0])
        finalSch += temp
        tempEnd = t[1]
        temp = [t]
temp = sorted(temp, key= lambda s: s[0])
finalSch += temp

print(sch)
print(finalSch)
now = 0
count = 0
for start, end in finalSch:
    print(now, start, end)
    if now <= start:
        count += 1
        now = end
print(count)



# # ValueError Occured.
# N = int(input())
# sch = []
# for _ in range(N):
#     s = tuple(map(int,input().split()))
#     sch.append(s)
# sch = sorted(sch, key=lambda s: s[1])

# numSch = [0 for _ in range(N)]
# indice = [0 for _ in range(N)]
# for i,t in enumerate(sch):
#     start, end = t[0],t[1]
#     indice[i] = t[1]
# #print(sch)
# #print(indice)
    
# for start, end in sch:
#     for i in range(N):
#         if start < indice[i]:
#             i -=1
#             break
#     print("i", i)
#     if i < 0:
#         numSch[indice.index(end)] = 1
#     elif i == 0:
#         numSch[indice.index(end)] = numSch[indice.index(start)] + 1
#     else:
#         numSch[indice.index(end)] = max(numSch[:i+1])+1
#     print(numSch)
# print(max(numSch))
