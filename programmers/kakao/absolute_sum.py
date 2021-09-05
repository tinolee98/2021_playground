# 정수 더하기: 절댓값과 부호가 두 개의 리스트로 주어졌을 때, 이들을 이용하여 총 합을 구하기

def solution(absolutes, signs):
    answer = 0
    for absolute, sign in zip(absolutes, signs):
        if sign:
            answer += absolute
        else:
            answer -= absolute
    return answer

lst = [[[4, 7, 12], [True, False, True]], [[1, 2, 3], [False, False, True]]]
answer = [9,0]
answer_sheet = []
for item in lst:
    answer_sheet.append(solution(item[0], item[1]))
if answer == answer_sheet:
    print("true")
else:
    print("false")