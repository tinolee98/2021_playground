# 체육복 빌리기 문제: 체육복이 없는 학생 번호 리스트와 여분의 체육복이 있는 학생 번호 리스트를 받아 얼마나 많은 학생들이 체육복을 입을 수 있는지 출력하라
# 단, 체육복은 자신의 앞뒤 번호인 학생에게만 빌릴 수 있다.
def solution(n, lost, reserve):
    for i in reserve:
        if i in lost:
            reserve.pop(reserve.index(i))
            lost.pop(lost.index(i))
    answer = n - len(lost)
    for i in lost:
        if i == 1 and i+1 in reserve:
            answer += 1
            reserve.pop(reserve.index(i+1))
        elif i == n and i-1 in reserve:
            asnwer += 1
            reserve.pop(reserve.index(i-1))
        elif i-1 in reserve:
            answer += 1
            reserve.pop(reserve.index(i-1))
            continue
        elif i+1 in reserve:
            answer += 1
            reserve.pop(reserve.index(i+1))
    return answer

n = int(input("n : "))
lost = list(map(int,input("lost : ").split()))
reserve = list(map(int,input("reserve : ").split()))
print(solution(n,lost,reserve))