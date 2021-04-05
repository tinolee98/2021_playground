# 큰 수 만들기: n에서 k개의 수를 제외시켜 가장 큰 수를 만들어라. ex) k=2, n=12345 -> result=345
def solution(k,number):
    n = list(map(int,number))
    print(n)
    lst = []
    finish = False
    while k > 0:
        while len(lst) < k:
            lst.append(n[0])
            del n[0]
            if len(n) == 0:
                break
            print(lst)
        while max(lst) == min(lst):
            if len(n) > 0:
                lst.append(n[0])
                del n[0]
            else:
                break
        if k != 1:
            print(lst[lst.index(min(lst))])
            del lst[lst.index(min(lst))]
        else:
            while len(n) > 0:
                lst.append(n[0])
                del n[0]
                print("k=1", lst)
                if lst[-1] > lst[-2]:
                    del lst[-2]
                    finish = True
                    break
            if not finish:
                del lst[-1]
        k -= 1
    #result = list(map(str,n))
    #print(result)
    #return ''.join(result)
    #lst = sorted(lst, reverse = True)
    result = lst + n
    result = map(str,result)
    print(''.join(result))
# 2139911, 4 
number = "1924"
k = 2
print(solution(k,number))
print()
number = "1231234"
k = 3
print(solution(k,number))
print()
number = "4177252841"
k = 4
print(solution(k,number))
number = "22222222222"
k = 4
print(solution(k,number))

# k번만큼 둘러보았을 때, 모두 같은 수인 경우 고려해야함
# 마지막 1번 남았을 때 하나씩 보다가 작은 수에서 큰 수가 나올 경우, 작은 수를 없에주어야함.