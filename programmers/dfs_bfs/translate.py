# 단어 변환: 주어진 words 리스트에서 begin부터 스펠링을 하나씩 바꿔가며 target을 만들어내기 위한 최소 변환 횟수를 리턴하자.

def solution(begin, target, words):
    answer = 0
    stack = [begin]
    visited = []
    while True:
        temp = []
        for now in stack:
            visited.append(now)
            if now == target:
                return answer
            for word in words:
                diff = sum([x != y for x,y in zip(now, word)])
                if diff == 1 and word not in visited:
                    temp.append(word)
        if not temp:
            return 0
        answer += 1
        stack = temp
    return answer

lst = [["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]], ["hit", "cog", ["hot", "dot", "dog", "lot", "log"]]]
answer_sheet = []
for item in lst:
    answer_sheet.append(solution(item[0],item[1],item[2]))

answer = [4,0]
if answer_sheet == answer:
    print("true")
else:
    print("false")