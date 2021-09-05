# 키패드 누르기: 양손의 엄지손가락으로 스마트폰의 숫자 키패드를 누르려고 한다. 왼손으로는 1,4,7을, 오른손으로는 3,6,9를, 두 엄지손가락 중 더 가까운 쪽으로 2,5,8,0을 누를 수 있다.
# 이때, 두 엄지손가락은 상하좌우 4방향으로만 움직일 수 있고, 2,5,8,0을 누르려할 때 거리가 같다면 어느 손잡이인지에 따라서 누르는 손가락이 달라진다.
def solution(numbers, hand):
    keypad = [[1,4,7,"*"], [2,5,8,0], [3,6,9,"#"]]
    l_place = (0,3)
    r_place = (2,3)
    answer = ''
    for n in numbers:
        if n in keypad[0]:
            l_place = (0, keypad[0].index(n))
            answer += 'L'
        elif n in keypad[2]:
            r_place = (2, keypad[2].index(n))
            answer += 'R'
        else:
            target = (1, keypad[1].index(n))
            l_dis = abs(l_place[0] - target[0]) + abs(l_place[1] - target[1])
            r_dis = abs(r_place[0] - target[0]) + abs(r_place[1] - target[1])
            if l_dis < r_dis:
                l_place = target
                answer += 'L'
            elif l_dis > r_dis:
                r_place = target
                answer += 'R'
            else:
                if hand == "right":
                    r_place = target
                    answer += 'R'
                else:
                    l_place = target
                    answer += 'L'
    return answer

lst = [[[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"], [[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"], [[1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"]]
answer = ["LRLLLRLLRRL", "LRLLRRLLLRR", "LLRLLRLLRL"]
answer_sheet = []
for itemList in lst:
    answer_sheet.append(solution(itemList[0], itemList[1]))
if answer == answer_sheet:
    print("true")
else:
    print("false")