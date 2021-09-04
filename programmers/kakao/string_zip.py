# 문자열 압축하기: 주어진 문자열을 맨 앞에서부터 일정 크기로 잘라서 반복되는 부분을 숫자를 활용하여 압축하려한다.
def solution(s):
    count_lst = ['' for _ in range(len(s)//2+1)]
    count_lst[0] = s
    for l in range(len(s)//2+1):
        temp = ''
        count = 1
        if l == 0:
            continue
        p = s[:l]
        for j in range(l,len(s), l):
            if p != s[j:j+l]:
                if count > 1:
                    temp += str(count)
                temp += p
                count = 1
                p = s[j:j+l]
            else:
                count += 1
        if count > 1:
            temp += str(count)
        temp += p
        count_lst[l] += temp
    answer = []
    for item in count_lst:
        answer.append(len(item)) 
    return min(answer)

lst = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", "xababcdcdababcdcd"]
answer_sheet = []
for item in lst:
    answer_sheet.append(solution(item))

answer = [7,9,8,14,17]
if answer_sheet == answer:
    print("true")
else:
    print("false")