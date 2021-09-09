# 멀쩡한 사각형: w*h인 직사각형에서 꼭짓점 간의 대각선으로 사각형을 잘랐을 때, 이에 영향을 받는 1*1 정사각형을 제외하면 몇개의 1*1 정사각형들이 남는가?

def GCD(a,b):
    return b if a%b == 0 else GCD(b,a%b)
    
def solution(w,h):
    Max = max(w,h)
    Min = min(w,h)
    gcd = GCD(Max, Min)
    a,b = Max/gcd, Min/gcd
    
    remove = Max if Max%Min == 0 else ((a//b+1)*b + a%b-1)*gcd
    return w*h-remove

lst = [[8,12]]
answer_sheet = []
for item in lst:
    answer_sheet.append(solution(item[0], item[1]))

answer = [80]
if answer_sheet == answer:
    print("true")
else:
    print("false")