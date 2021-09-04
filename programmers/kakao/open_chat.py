# 오픈 채팅방: 누군가 들어오고 나갈 때 채팅방에는 기록이 남는다. enter, leave, change를 통해 사람들은 채팅방에 들어올 수도, 나갈 수도, 닉네임을 바꿀 수도 있다.
# 같은 사람이 다시 들어올 때 닉네임을 바꾸어서 들어오게 된다면, 이전의 기록들의 닉네임도 모두 새로운 것으로 변경이 된다.

def enterOrChange(id, nickname, dic):
    dic[id] = nickname

def solution(record):
    history = []
    nickname = {}
    for item in record:
        command = item.split()
        if command[0] == "Enter":
            enterOrChange(command[1], command[2],nickname)
            history.append((command[0], command[1]))
        elif command[0] == "Change":
            enterOrChange(command[1], command[2], nickname)
        else:
            history.append((command[0], command[1]))
    string_dic = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
    answer = []
    for command, id in history:
        answer.append("{}{}".format(nickname[id], string_dic[command]))
    
    return answer

lst = [["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]]
answer = [["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]]
answer_sheet = []
for i in lst:
    answer_sheet.append(solution(i))

if answer_sheet == answer:
    print("true")
else:
    print("false")