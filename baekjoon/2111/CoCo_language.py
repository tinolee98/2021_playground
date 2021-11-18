# This problem is not in Baekjoon.
import heapq
wordsList = [['xwt','xwf','aw','att','wftt'], ['a','l'], ['a','l','a']]
outputs = ["xawtf", "al", ""]

# def solution(words, output):
#     result = []
#     last = words[0]
#     check = [last[0]]
#     linked = [1]
#     solOk = True
#     for word in words[1:]:
#         print(last, word)
#         if not check:
#             break
#         for i in range(len(last)):
#             if last[i] != word[i]:
#                 if last[i] not in check and word[i] not in check:
#                     check.append(last[i])
#                     linked.append(len(check))
#                     check.append(word[i])
#                     linked.append(len(check))
#                 elif last[i] not in check:
#                     check.append(last[i])
#                     linked[linked.index(check.index(word[i]))] = len(check)-1
#                     linked.append(check.index(word[i]))
#                 elif word[i] not in check:
#                     next = linked[check.index(last[i])]
#                     check.append(word[i])
#                     linked.append(next)
#                     print("test",linked)
#                     print(check.index(last[i]))
#                     linked[check.index(last[i])] = len(check)-1
#                     print("!!!!!!", linked)
#                 else:
#                     j = linked[check.index(last[i])]
#                     visited = [False for _ in range(len(check))]
#                     while solOk:
#                         print(check)
#                         print(linked[j], linked)
#                         if j >= len(check) or visited[j]:
#                             solOk = False
#                             break
#                         if check[j] == word[i]:
#                             print("check[j] == word[i]")
#                             break
#                         visited[j] = True
#                         j = linked[j]
#                     if not solOk:
#                         check = []
                        
#                 break
#         print("check", check)
#         print("linked", linked)
#         last = word
#     visited = [False for _ in range(len(check))]
#     i = 0
#     ok = True
#     while ok:
#         if i >= len(check) or visited[i]:
#             break
#         result.append(check[i])
#         visited[i] = True
#         i = linked[i]
#     result = ''.join(result)
#     if solOk:
#         for word in words:
#             for c in word:
#                 if c not in result:
#                     result += c

#     print("result",result)
#     if output == result:
#         print("success")
#     else:
#         print("fail")

def solution(words, output):
    pass

for words, output in zip(wordsList, outputs):
    solution(words, output)
    
testList = list(input().split())
solution(testList,[])