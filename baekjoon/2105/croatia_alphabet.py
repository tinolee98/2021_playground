# 크로아티아 알파벳: 크로아티아 알파벳을 표현하기 위해 2개 이상의 문자를 사용하였다. 총 사용된 문자의 개수를 출력하라.

a = input()
cnt = 0
i = 0
while i < len(a):
    try:
        if a[i:i+2] in ['c=','c-','nj','lj','d-','s=','z=']:
                #print(a[i:i+2])
                i += 1 
        elif a[i:i+3] == 'dz=':
                #print(a[i:i+3])
                i += 2
        i += 1
        cnt += 1
    except:
        i += 1
        cnt += 1
print(cnt)