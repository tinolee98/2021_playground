# 2021 kakao blind recruit 1번 문제 // 정규식으로 풀면 더 쉬운 문제였네요.
# 신규 아이디 추천
import sys
def solution(new_id):
    print('0',new_id)
    # level 1
    new_id = new_id.lower()
    print('1',new_id)
    # level 2
    memo = ['-','_','.']
    temp_id = ''
    for e in new_id:
        if e.isalnum() or e in memo:
            temp_id += e
    print('2',temp_id)
    # level 3
    new_id = ''
    repeat = False
    for e in temp_id:
        if e != '.':
            repeat = False
            new_id += e
        elif e == '.' and repeat is False:
            new_id += e
            repeat = True
    print('3',new_id)
    # level 4
    temp_id = ''
    for i,e in enumerate(new_id):
        if (i == 0 or i == len(new_id)-1) and e == '.':
            continue
        temp_id += e
    print('4',temp_id)
    # level 5
    if temp_id == '':
        temp_id = 'a'
    print('5',temp_id)
    # level 6
    if len(temp_id) >= 16:
        temp_id = temp_id[:15]
    if temp_id[-1] == '.':
        temp_id = temp_id[:len(temp_id)-1]
    print('6',temp_id)
    # level 7
    temp = temp_id[-1]
    while len(temp_id) < 3:
        temp_id += temp
    print('7',temp_id)

    answer = temp_id
    return answer

#new_id = sys.stdin.readline().strip()
#new_id = "...!@BaT#*..y.abcdefghijklm."
#new_id = "z-+.^."
new_id = "abcdefghijklmn.p"
recommand = solution(new_id)
print(recommand)