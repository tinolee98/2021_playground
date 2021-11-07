import sys
N = int(input())
M = int(input())
input = sys.stdin.readline
lst = input().rstrip()

# KMP 활용하기
def piFunc(n):
    print("IO"*N + "I")
    pi = [0 for _ in range(2*N+1)]
    for i in range(len(pi)):
        pi[i] = i+1 if i%2 == 0 else 0
    return pi
print(piFunc(N))


# 단순 무식하기 풀어버리기!
# lst = ' '.join(list(input().rstrip()))
# lst = lst.replace("I","1")
# lst = lst.replace("O","0")
# lst = list(map(int,lst.split()))

# lst1 = []
# lst2 = []
# for i in range(len(lst)):
#     if i%2 == 0:
#         lst1.append(lst[i])
#     else:
#         lst2.append(lst[i])
# #print(lst1)
# #print(lst2)
# count = 0
# i = 0
# while i < len(lst1):
#     if i+N < len(lst1):
#         can = sum(lst1[i:i+N+1]) == N+1 and sum(lst2[i:i+N]) == 0
#         if can:
#             count += 1
#             i += 1
#         else:
#             i += N
#     else:
#         break
# i = 0
# for i in range(len(lst2)):
#     if i+N < len(lst2):
#         can = sum(lst1[i+1:i+N+1]) == 0 and sum(lst2[i:i+N+1]) == N+1
#         if can:
#             count += 1
#             i += 1
#         else:
#             i += N
#     else:
#         break

# print(count)