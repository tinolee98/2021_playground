# 큰 수 만들기: n에서 k개의 수를 제외시켜 가장 큰 수를 만들어라. ex) k=2, n=12345 -> result=345
def solution(k,number):
    n = list(map(int,number))
    print(n)
    while k > 0:
        print('k',k)
        i = 0
        if k == 1:
            m = n[0]
            for i in range(len(n)):
                if m >= n[i]:
                    m = n[i]
                else:
                    del n[i-1]
                    break
        else:
            lst = n[:k]
            print(lst)
            if min(lst) == lst[0]:  # 같은 수 반복
                j = k
                while j <= len(n):
                    if n[j] > lst[0]:
                        del n[0]
                        break
                    elif n[j] == lst[0]:
                        j += 1
                        continue
                    else:
                        del n[j]
                        break            
            else:
                del n[lst.index(min(lst))]
            #for i in range(k):                
        #print("del",n[j])
        #del n[j]
        #min_ = 0
        #for i in range(k):
        #    if min(min_,int(n[k])):
        #        min_ = int(n[k])
        #del n[n.index(chr(min_))]
        k -= 1
        print(n)
    result = list(map(str,n))
    print(result)
    return ''.join(result)

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

# k번만큼 둘러보았을 때, 모두 같은 수인 경우 고려해야함
# 마지막 1번 남았을 때 하나씩 보다가 작은 수에서 큰 수가 나올 경우, 작은 수를 없에주어야함.