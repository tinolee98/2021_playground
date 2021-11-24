s1 = input()
s2 = input()
memo = [(-1,0)]
test = [0]*len(s2)
maximum = 0
for k,std in enumerate(s1):
    temp = [0]*len(s2)
    for i,c in enumerate(s2):
        if std == c:
            if i != 0:
                temp[i] = max(test[:i])+1
            if temp[i] == 0:
                temp[i] = 1
    for i,n in enumerate(temp):
        if n != 0:
            test[i] = n
    # print(temp)
    # print(std,test)
    # print("memo",memo)
print(max(test))