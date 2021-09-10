# 뉴스 클러스터링
from math import floor

def Slice(s):
    result = {}
    for i in range(len(s)-1):
        two = ''.join(s[i:i+2])
        two = two.lower()
        if two.isalpha():
            if two not in result:
                result[two] = 1
            else:
                result[two] += 1
    return result
    
def solution(str1, str2):
    answer = 0
    sl1 = Slice(str1)
    sl2 = Slice(str2)
    #print(sl1)
    #print(sl2)
    inter_set = set(sl1).intersection(set(sl2))
    union_set = set(sl1).union(set(sl2))
    #print(inter_set)
    #print(union_set)
    j1, j2 = 0, 0
    for i in inter_set:
        j1 += min(sl1[i], sl2[i])
    for i in union_set:
        if i in sl1 and i not in sl2:
            j2 += sl1[i]
        elif i not in sl1 and i in sl2:
            j2 += sl2[i]
        else:
            j2 += max(sl1[i], sl2[i])
    if j2 == 0 and j1 == 0:
        return 65536
    return floor(j1/j2*65536)

lst = [["FRANCE","french"], ["handshake", "shake hands"], ["aa1+aa2", "AAAA12"], ["E=M*C^2", "e=m*c^2"]]
answer = [16384, 65536, 43690,65536]
answer_sheet = []
for item in lst:
    answer_sheet.append(solution(item[0], item[1]))
if answer == answer_sheet:
    print("true")
else:
    print("false")