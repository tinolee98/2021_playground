# 2021 kakao blind recruit 5번 문제
# 광고 삽입

def solution(play_time, adv_time, logs):
    answer = ''
    play = list(map(int, play_time.split(':')))
    play_time = play[0]*60*60+play[1]*60+play[2]
    adv = list(map(int, adv_time.split(":")))
    adv_time = adv[0]*3600+adv[1]*60+adv[2]
    print(play_time, adv_time)
    # 영상시간과 광고시간이 같은 경우
    if play_time == adv_time:
        return "00:00:00"

    temp_log = []
    for log in logs:
        temp = list(map(str, log.split("-")))
        temp2 = []
        for i in range(2):
            lst = list(map(int, temp[i].split(":")))
            temp2.append(lst[0]*3600 + lst[1]*60 + lst[2])
        temp_log.append(temp2)
    logs = temp_log
    print(logs)

    # second로 치환하는 작업은 끝! logs의 시작시간부터 adv_time만큼 흘렀을 때 각각 누적시간을 구해서 가장 높은 것에 배치하면 된다!
    # 만약 마지막 부분에 몰려있다면 가장 마지막 부분에서 adv_tiem만큼 빠른 시각에서 시작하면 된다 (예외)

    return answer

play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
print(solution(play_time, adv_time, logs))