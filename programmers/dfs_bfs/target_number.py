# 타겟 넘버: numbers가 주어지면, 이들을 서로 더하거나 빼면서 target을 만든다. 이때, 만들 수 있는 방법의 수를 리턴하자.

from collections import deque
def solution(numbers, target):
    queue = deque()
    for n in numbers:
        if len(queue) == 0:
            queue.append(n)
            queue.append(-n)
        else:
            for _ in range(len(queue)):
                m = queue.popleft()
                queue.append(m-n)
                queue.append(m+n)
    answer = list(queue).count(target)
    return answer

lst = [[[1, 1, 1, 1, 1], 3]]
answer_sheet = []
for item in lst:
    answer_sheet.append(solution(item[0], item[1]))

answer = [5]
if answer_sheet == answer:
    print("true")
else:
    print("false")