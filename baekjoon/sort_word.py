# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

# 1. 길이가 짧은 것부터
# 2. 길이가 같으면 사전 순으로
N = int(input())
words = []
memo = {}
result = []
for i in range(N):
    words.append(str(input()))
#print(words)
for word in words:
    if len(word) in memo and not word in memo[len(word)]:
        memo[len(word)].append(word)
    else:
        memo[len(word)] = [word]
#print(memo)
for i in range(51):
    if i in memo:
        temp = memo[i]
        temp.sort()
        result.extend(temp)
print('\n'.join(result))