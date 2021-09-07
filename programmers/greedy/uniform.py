# 체육복 빌리기 문제: 체육복이 없는 학생 번호 리스트와 여분의 체육복이 있는 학생 번호 리스트를 받아 얼마나 많은 학생들이 체육복을 입을 수 있는지 출력하라
# 단, 체육복은 자신의 앞뒤 번호인 학생에게만 빌릴 수 있다.
def solution(n, lost, reserve):
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)
    for i in new_lost:
        if i-1 in new_reserve:
            new_reserve.remove(i-1)
        elif i+1 in new_reserve:
            new_reserve.remove(i+1)
        else:
            n -= 1
    return n

n = int(input("n : "))
lost = list(map(int,input("lost : ").split()))
reserve = list(map(int,input("reserve : ").split()))
print(solution(n,lost,reserve))

# 런타임 에러 및 몇몇 케이스에서 작동되지 않는다!