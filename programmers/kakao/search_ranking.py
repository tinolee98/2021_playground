# # 2021 kakao blind recruit 3번 문제
# 순위 검색
import sys

def solution (info, query):
    lst_query = []
    for q in query:
        lst_query.append(list(map(str,q.split())))
    query = []
    for q in lst_query:
        temp = []
        for p in q:
            if p != 'and':
                temp.append(p)
        query.append(temp)
    print(query)
    print("---")
    lst_info = []
    for q in info:
        lst_info.append(list(map(str,q.split())))
    print(lst_info)
    info = lst_info
    answer = []

    # 이제 비교만 하면 됩니다.
    for i in query:
        for j in range(len(i)):
            standard = i[j]
            for k in info:
                pass
    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))