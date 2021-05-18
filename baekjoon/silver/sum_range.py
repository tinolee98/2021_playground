# 동호 대신 수열 더하기 / 1 22 333 4444 처럼 나열된 수열을 임의의 위치까지 더해서 결과를 출력
a,b = map(int,input().split())
array = []
cnt = 0
result = 0
for i in range(1,46):
    for j in range(i):
        cnt += 1
        #print("cnt", cnt, "i", i)
        if a <= cnt and cnt <= b:
            result += i
        elif cnt > b:
            break
    #print(result)
print(result)