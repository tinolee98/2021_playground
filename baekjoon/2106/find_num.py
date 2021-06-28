# 수찾기: 주어진 수들 중 찾고자 하는 수가 있다면 1을, 없다면 0을 출력

def bs(lst, find, first, last):
    middle = (first+last)//2
    #print(first, middle, last, "find", find)
    if first > last:
        return 0
    elif lst[middle] == find:
        return 1
    elif lst[middle] > find:
        return bs(lst,find,first,middle-1)
    else:
        return bs(lst,find,middle+1,last)


n = int(input())
lst = list(map(int, input().split()))
lst.sort()
m = int(input())
find = list(map(int, input().split()))

for f in find:
    if f > lst[-1]:
        print(0)
    else:
        print(bs(lst,f,0,n))