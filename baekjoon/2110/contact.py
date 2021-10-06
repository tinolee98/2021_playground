# (100+1+ | 01)+

T = int(input())
signals = []
for _ in range(T):
    signals.append(input())

def DFA(signal):
    state = "S"
    # 0: start
    # 1: 처음에 1을 읽은 상태
    # 2: 처음에 0을 읽은 상태
    # 3: 1을 읽고 0을 읽은 상태
    # 4: 실패
    for n in signal:
        #print(state)
        if state == 'S':
            if n == '1':
                state = 'A'
            elif n == '0':
                state = 'B'

        elif state == 'A':
            if n == '1':
                state = "fail"
            elif n == '0':
                state = "C"

        elif state == 'B':
            if n == '1':
                state = "ok"
            elif n == '0':
                state = "fail"

        elif state == 'C':
            if n == '1':
                state = "fail"
            elif n == '0':
                state = "D"

        elif state == 'D':
            if n == '1':
                state = "E"
            elif n == '0':
                state = "D"

        elif state == 'E':
            if n == '1':
                state = "F"
            elif n == '0':
                state = "B"

        elif state == 'F':
            if n == '1':
                state = "F"
            elif n == '0':
                state = "G"

        elif state == 'G':
            if n == '1':
                state = "ok"
            if n == '0':
                state = "D"

        elif state == "fail":
            return "NO"

        elif state == "ok":
            if n == '1':
                state = "A"
            elif n == '0':
                state = "B"

    if state in ["ok", 'F', 'E']:
        return "YES"
    return "NO"


for signal in signals:
    #print(program(signal))
    print(DFA(signal))
        