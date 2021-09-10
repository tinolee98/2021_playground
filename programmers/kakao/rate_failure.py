# 실패율

def solution(N, stages):
    lst = [0 for _ in range(N+2)]
    answer = [[i for i in range(1,N+2)],[]]
    for i in stages:
        lst[i] += 1
    #print(lst)
    for i in range(1,N+1):
        s = sum(lst[i:])
        if s == 0:
            answer[1].append(0)
        else:
            answer[1].append(lst[i]/s)
    answer[0], answer[1] = answer[0][:N], answer[1][:N]
    #print(answer)
    result = []
    for _ in range(N):
        maximum = max(answer[1])
        for i in range(N):
            if answer[1][i] == maximum:
                result.append(answer[0][i])
                answer[1][i] = -1
                break
    #    print("answer", answer)
    #    print("result", result)
    
    return result

lst = [[5, [2, 1, 2, 6, 2, 4, 3, 3]], [4, [4, 4, 4, 4, 4]], [3, [1, 1, 1, 1, 1]]]
answer = [[3, 4, 2, 1, 5], [4, 1, 2, 3], [1, 2, 3]]
answer_sheet = []
for item in lst:
    answer_sheet.append(solution(item[0], item[1]))
if answer == answer_sheet:
    print("true")
else:
    print("false")