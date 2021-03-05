# ()가 짝을 이룰 수 있다면 true, 아니라면 false 를 return
# 0 <= input.length <= 100
temp = input(">> ")
st = []
a = ['(',')']
for i in temp:
    if i in a:
        if len(st) == 0 or i == '(':
            st.append(i)
        elif st[-1] == '(' and i == ')':
            st.pop()
    print(i,st)
if len(st) == 0:
    print(True)
else:
    print(False)