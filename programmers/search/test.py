# 모의고사: 1,2,3번 수포자는 제각기 자신만의 방법으로 모의고사를 찍는다. 가장 많이 맞춘 사람(들)을 리턴하자.

def solution(answers):
    supojar = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    result = []
    for way in supojar:
        count = 0
        for i in range(len(answers)):
            if answers[i] == way[i%len(way)]:
                count += 1
        result.append(count)
    highest = max(result)
    answer = []
    for i in range(3):
        if result[i] == highest:
            answer.append(i+1)
    return answer

lst = [[1, 2, 3, 4, 5], [1, 3, 2, 4, 2]]
answer_sheet = []
for item in lst:
    answer_sheet.append(solution(item))

answer = [[1], [1,2,3]]
if answer_sheet == answer:
    print("true")
else:
    print("false")