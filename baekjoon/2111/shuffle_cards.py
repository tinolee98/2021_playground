from copy import deepcopy
N = int(input())
S = list(map(int, input().split()))
P = list(map(int, input().split()))
std = deepcopy(S)

def Check(cards):
    for i in range(N):
        if cards[i] != i%3:
            return False
    return True

def Shuffle(cards):
    # print("Shuffle")
    temp = [0 for _ in range(N)]
    for i,j in enumerate(P):
        temp[j]=cards[i]
    # print(temp)
    return temp
count = 0
while not Check(S):
    cards = Shuffle(S)
    if std == cards:
        count = -1
        break
    S = cards
    # print(S,std)
    count += 1
print(count)