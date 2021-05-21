# 그룹단어체커: 한번 나온 단어가 불연속적으로 나오면 체크 X.

n = int(input())
lst = []
for i in range(n):
    lst.append(str(input()))
cnt = 0
for s in lst:
    memo = {}
    temp = ''
    for i in range(len(s)):
        if i == 0:
            memo[s[i]] = 1
        elif s[i] in memo and s[i] != temp :
            cnt -= 1
            break
        else:
            memo[s[i]] = 1
        temp = s[i]
    cnt +=1
print(cnt)