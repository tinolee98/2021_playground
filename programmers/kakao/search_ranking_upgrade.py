# # 2021 kakao blind recruit 3번 문제
# 순위 검색
import sys

def solution (info, query):
    '''answer = []
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
    info = lst_info'''
    answer = []
    lst_query = []
    for q in query:
        lst_query.append(list(map(str, q.split())))
    query = lst_query
    lst_info = []
    for q in info:
        lst_info.append(list(map(str, q.split())))
    info = lst_info
    print(query, info)
    # 이제 비교만 하면 됩니다.
    for q in query:
        test = []
        cnt = 0
        for l in range(0,len(q),2):
            print(l)
            if q[l] == '-':
                print('-')
                continue
            for i in range(len(info)):
                print(info[i][l//2])
                if i in test:
                    print("continue")
                    continue
                elif l != len(q) and q[l] != info[i][l//2]:
                    print("!!!!append")
                    test.append(i)
                    continue
                elif l == len(q) and int(q[l]) <= int(info[i][l//2]):
                    cnt += 1
                    print("l", l, "i", i)
                    print("q[l]", q[l], "info[i][l]", info[i][l])
                    print(cnt) # 이렇게 푸는 문제는 아닌거 같습니다.
            print("end",test)
        print("cnt",cnt)
        answer.append(cnt)
    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))