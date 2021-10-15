A,B,C = list(map(int, input().split()))

def divide(A,B,C,result):
    if B == 1:
        #print(A,B,C,result)
        return result*A%C
    if B%2 == 1:
        result *= A
        #print((A%C)**2,B//2,C,result)
        return divide((A%C)**2,B//2,C,result)
    else:
        #print((A%C)**2,B//2,C,result)
        return divide((A%C)**2,B//2,C,result)

result = 1
print(divide(A,B,C,result))